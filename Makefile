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

run_deployed_locally: fmt tests
	echo "Running deployed model locally"
	export FLASK_APP=deploy/app.py
	pipenv run flask run --port 8000

test_deploy: fmt tests
	echo "Testing deployed model"
	pipenv run python deploy/test.py

prefect_start: fmt tests
	pipenv run prefect orion start

prefect_deploy: fmt tests
	pipenv run prefect deployment create orchestration/prefect/train_lr.py

prefect_run: fmt tests
	pipenv run python -m orchestration.prefect
