import logging

from pathlib import Path
from typing import List
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression

from logger import init_logger
from etl.extract import load_data
from etl.transform import preprocess_data



init_logger(Path("..", "logs", "linear_regression.log"))
logger = logging.getLogger("main")

def pipeline_steps() -> Pipeline:
    steps = [
            ("dictvectorizer", DictVectorizer()),
            ("linearregression", LinearRegression())
            ]
    
    return Pipeline(steps=steps)


def train(year: int, month: int, cat_columns: List[str]=["PULocationID", "DOLocationID"], target="duration") -> Pipeline:
    features = []
    df = load_data(year=year, month=month)
    process_df = preprocess_data(df)
    pipe = pipeline_steps()
    
    train_dicts = process_df[cat_columns].astype(str).to_dict(orient="records")
    features.extend(cat_columns)
    
    y = process_df[target].values
    pipe.fit(train_dicts, y)
    
    return pipe