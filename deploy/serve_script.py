import mlflow
from load import get_model

TRACKING_URI = "http://127.0.0.1:5000"

mlflow.set_tracking_uri(TRACKING_URI)
client = mlflow.MlflowClient()

model = get_model(model_stage="Staging", client=client)
