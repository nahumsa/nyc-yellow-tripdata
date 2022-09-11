from typing import List, Tuple

import mlflow
import numpy as np
import pandas as pd
from flask import Flask, jsonify, request
from load import get_model

app = Flask("taxi-prediction")

TRACKING_URI = "http://127.0.0.1:5000"
MODEL_VERSION = "None"

mlflow.set_tracking_uri(TRACKING_URI)
client = mlflow.MlflowClient()
model, version_model = get_model(model_stage=MODEL_VERSION, client=client)


def process_data(
    df: pd.DataFrame, cat_columns: List[str] = ["PULocationID", "DOLocationID"]
) -> Tuple[pd.DataFrame, np.array]:
    """Process the data for the model using the `etl.preprocess_data` and generate the input
    for the DictVectorizer

    Args:
        df (pd.DataFrame): data to process
        cat_columns (List[str]): categorical columns on the dataset

    Returns:
        pd.DataFrame: processed dataframe
        np.array: entry for the dict vectorizer
    """
    process_df = df.copy()
    return process_df[cat_columns].astype(str).to_dict(orient="records")


@app.route("/predict", methods=["POST"])
def predict_length():
    ride = request.get_json()

    ride_data = process_data(pd.DataFrame([ride]))

    result = {
        "duration": model.predict(ride_data)[0],
        "model_version": version_model.version,
        "model_name": version_model.name,
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
