DATABASE_URI="sqlite:///mlflow.db"
ARTIFACTS_FOLDER="artifacts"

mlflow server \
    --backend-store-uri $DATABASE_URI \
    --default-artifact-root $ARTIFACTS_FOLDER 