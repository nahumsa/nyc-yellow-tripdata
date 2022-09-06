import logging
from pathlib import Path
from typing import List, Tuple

import mlflow
import numpy as np
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.pipeline import Pipeline

from etl.extract import load_data
from etl.transform import preprocess_data

mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("linear-regression")


def pipeline_steps() -> Pipeline:
    """Generate pipeline for linear regression

    Returns:
        Pipeline: DictVectorizer + LinearRegression
    """
    steps = [
        ("dictvectorizer", DictVectorizer()),
        ("linearregression", LinearRegression()),
    ]

    return Pipeline(steps=steps)


def process_data(df: pd.DataFrame, cat_columns: List[str]) -> Tuple[pd.DataFrame, np.array]:
    """Process the data for the model using the `etl.preprocess_data` and generate the input
    for the DictVectorizer

    Args:
        df (pd.DataFrame): data to process
        cat_columns (List[str]): categorical columns on the dataset

    Returns:
        pd.DataFrame: processed dataframe
        np.array: entry for the dict vectorizer
    """
    process_df = preprocess_data(df)
    return process_df, process_df[cat_columns].astype(str).to_dict(orient="records")


def eval_metrics(actual: List[float], pred: List[float]) -> Tuple[float, float, float]:
    """Calculate evaluation metrics: rmse, mae, r2.

    Args:
        actual (List[float]): actual data
        pred (List[float]): predicted data

    Returns:
        float: root mean squared error
        float: mean absolute error
        float: r2
    """
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2


def train_and_valid(
    year: int,
    month: int,
    cat_columns: List[str] = ["PULocationID", "DOLocationID"],
    target="duration",
) -> Tuple[Pipeline, List[str]]:
    """Train and validate the

    Args:
        year (int): year for training. The validation data will be in the same year.
        month (int): month for training. The validation data will be in the next month.
        cat_columns (List[str], optional): categorical columns used. Defaults to ["PULocationID", "DOLocationID"].
        target (str, optional): target variable. Defaults to "duration".

    Returns:
        Pipeline: model pipeline with the DictVectorizer + linear regression
        List[str]: Features used for inference
    """

    features = []

    df_train = load_data(year=year, month=month)
    df_valid = load_data(year=year, month=month + 1)

    mlflow.autolog()
    pipe = pipeline_steps()

    process_df_train, train_dicts = process_data(df_train, cat_columns=cat_columns)
    features.extend(cat_columns)

    y = process_df_train[target].values
    pipe.fit(train_dicts, y)

    process_df_valid, valid_dicts = process_data(df_valid, cat_columns=cat_columns)
    y_valid = process_df_valid[target].values
    valid_prediction = pipe.predict(valid_dicts)

    rmse, mae, r2 = eval_metrics(y_valid, valid_prediction)

    mlflow.log_metric("valid_rmse", rmse)
    mlflow.log_metric("valid_r2", r2)
    mlflow.log_metric("valid_mae", mae)

    return pipe, features
