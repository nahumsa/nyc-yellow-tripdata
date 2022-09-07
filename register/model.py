import mlflow
from mlflow import MlflowClient
from mlflow.entities.model_registry.model_version import ModelVersion


def register_model_from_run_id(
    run: str, uri: str, model_name: str = "nyc-yellow-trip"
) -> ModelVersion:
    """Register a model from a run.

    Args:
        run (str): run of a given experiment in the mlflow client.
        uri (str): mlflow client tracking uri
        model_name (str): name of the model in the model registry

    Returns:
        ModelVersion: Registered model version.
    """
    mlflow.set_tracking_uri(uri)
    model_uri = "runs:/" + run.info.run_id

    return mlflow.register_model(
        model_uri=model_uri,
        name=model_name,
    )


def transition_motor_model(
    version: int,
    model_stage: str,
    uri: str,
    model_name: str = "nyc-yellow-trip",
) -> bool:
    """Transition a model in the model registry.

    Args:
        version (int): version of the model
        model_stage (str): stage where the model is: `Staging`, `Production`, `None`.
        uri (str): mlflow client tracking uri

    Returns:
        bool: True if the model was properly transitioned
    """

    client = MlflowClient(tracking_uri=uri)

    try:
        client.transition_model_version_stage(
            name=model_name, version=version, stage=model_stage
        )
        return True

    except:
        return False
