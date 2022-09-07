tests:
	pipenv run tests

fmt:
	pipenv run fmt

setup:
	pipenv install --dev
	pipenv run pre-commit install

start_mlflow:
	pipenv run sh scripts/launch_mlflow_server.sh

train: fmt tests
	echo "Training the model"
	pipenv run python -m models
