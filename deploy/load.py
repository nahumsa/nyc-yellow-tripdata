import mlflow
from mlflow.pyfunc import PyFuncModel
from mlflow.tracking.client import MlflowClient


def get_model(
    model_stage: str, client: MlflowClient, model_name: str = "nyc-yellow-trip"
) -> PyFuncModel:
    """Load the latests version of the motor model from the mlflow tracking uri given the model name, variable, kind of model, and model stage.

    Args:
        motor (str): motor name
        variable (str): variable of the model
        kind (str): kind of model
        model_stage (str): stage where the model is: `Staging`, `Production`
        client (MlflowClient): client for the mlflow tracking.

    Returns:
        PyFuncModel: Mlflow model that has `.predict` method
    """
    model = client.get_latest_versions(model_name, stages=[model_stage])[0]

    return mlflow.pyfunc.load_model(f"runs:/{model.run_id}/model"), model
