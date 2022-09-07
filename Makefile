tests:
	pipenv run tests

fmt:
	pipenv run fmt

setup:
	pipenv install --dev
	pipenv run pre-commit install

start_mlflow:
	pipenv run sh scripts/launch_mlflow_server.sh

train_lr: fmt tests
	echo "Training the model"
	pipenv run python -m models --model linear_regression

register_best_model: fmt tests
	echo "Registering the best model"
	pipenv run python -m register
