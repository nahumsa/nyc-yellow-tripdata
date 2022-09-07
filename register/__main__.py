from typing import List

import mlflow
from mlflow import MlflowClient
from mlflow.entities.model_registry.model_version import ModelVersion

from .model import register_model_from_run_id

TRACKING_URI = "http://127.0.0.1:5000"

mlflow.set_tracking_uri(TRACKING_URI)


def list_runs_from_experiment(experiment_name: str) -> List[ModelVersion]:
    """List all runs in descending order for the validation MAE.

    Args:
        experiment_name (str): name of the experiment in the mlflow client

    Returns:
        List[ModelVersion]: models in descending order of the validation MAE
    """

    client = MlflowClient()
    experiment_id = client.get_experiment_by_name(experiment_name).experiment_id

    runs = []

    for run in client.search_runs(
        experiment_ids=[experiment_id], order_by=["metrics.valid_mae DESC"]
    ):
        runs.append(run)

    return runs


if __name__ == "__main__":
    EXPERIMENT_NAME = "nyc-yellow-taxi"
    all_runs = list_runs_from_experiment(experiment_name=EXPERIMENT_NAME)
    best_mae_run = all_runs[0]
    model = register_model_from_run_id(best_mae_run, uri=TRACKING_URI)
