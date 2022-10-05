<h1 align="center">Predicting the time for the NYC yellow taxi trip</h1>
<p align="center">
<a href="https://github.com/nahumsa/nyc-yellow-tripdata/actions"><img alt="Actions Status" src="https://github.com/nahumsa/nyc-yellow-tripdata/workflows/nyc-yello-taxi/badge.svg"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://pycqa.github.io/isort/"><img alt="Imports: isort" src="https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336"></a>
</p>

The main goal of the project is to develop MLOps skills, that is: Use experiment tracking, workflow orchestration, model registry, and deployment. Another plus is to use unit tests, integration tests, CI/CD. This will be demonstrated by creating and serving a model to predict the time based on the yellow taxi pickup and dropoff location, and other additional features.

# Problem statement

Humans are always concerned with time most of the time, mainly when we're commuting. It is common to take taxis when commuting, or simply going somewhere and, as stated before, we want to know how long the trip will take. In this project, I will use the data provided by [NYC Yellow Taxi Trip Records](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page) to generate a model for predicting the duration of the trip given the pickup and dropoff location.

# How to run the code

In order to run the code, you first need to install [`pipenv`](https://pipenv.pypa.io/en/latest/), then you can use `Makefile`. To prepare the environment of the project you can run:

```
make setup
```

This will install the dependencies using `pipenv` and the `pre-commit` hooks.

## Makefile

Each section is one of the makefile commands.

### start_mlflow

This will start the local MLFLOW server on host `http://127.0.0.1/` and port `5000`. This is needed to run the training scripts, and serve the deployed model.

### train_lr

This will train the linear regression model on the first month of the 2022, validates on the next month, and logs to MLFLOW.

### register_best_model

This will register the best model to the registry on the `nyc-yellow-taxi` on MLFLOW on `model_stage=None`.

### run_deployed_locally

This will start the flask server locally on port `8000`, the flask server has an endpoint `/predict` which receives a JSON with `PULocationID` and `DOLocationID`. You will need to run the `start_mlflow` in order to have model available for the endpoint, also you need to have to train and register a model by running `train_lr` and `register_best_model`.

### test_deploy

In order to run this command you have to do two things:
 - Run the `run_deployed_locally` command to spin up the local prediction endpoint.
 - Run the `start_mlflow` in order to have load the model available.

### prefect_start

This will start prefect orion on port `4200`.

### prefect_deploy

This will deploy the prefect flow for training the logistic regression model.

### prefect_run

This will run the prefect flow for training the logistic regression.

## Sample workflow for running this project

First, install pipenv

```
pip install pipenv
```

Then setup the local environment installing the dependencies and the pre-commit hooks
```
make setup
```

Start the mlflow server (now on, this needs to be in a seperated terminal):

```
make start_mlflow
```

Train the linear regression model:

```
make train_lr
```

Register the linear regression model (this works for the model with the best validation mean absolute error):
```
make register_best_model
```

This will register the model to the `stage=None` on the model registry.

Create the local deployment by starting the flask server:

```
make run_deployed_locally
```

Alternatively, you can run the docker-compose command:

```
docker-compose up -d --build
```
This will start the flask server on port `8000`.

In another terminal, you can test the local deployment:

```
make test_deploy
```

This should return a JSON just like this : `{'duration': 685.0228426897559, 'model_name': 'nyc-yellow-trip', 'model_version': '2'}`


## Caveat for the Dockerfile

In the deployment Dockerfile, I import the `artifacts` folder created from MLFLOW, this is done because I need it to load the model inside the docker container. This could be easily avoided by using a s3 bucket as the artifact store, however, sadly, I do not have the resources to use any cloud infraestructure.

An improvement will be to use [`localstack`](https://github.com/localstack/localstack) to mock the s3 bucket that keeps the artifacts for MLFLOW.

## Folder structure

In this project, there are the following folders:

- [etl](https://github.com/nahumsa/nyc-yellow-tripdata/tree/main/etl): Which is responsible for data preprocessing and loading.
- [deploy](https://github.com/nahumsa/nyc-yellow-tripdata/tree/main/deploy): The script for the flask application that uses the model to make predictions
- [data](https://github.com/nahumsa/nyc-yellow-tripdata/tree/main/data): Where the data is stored
- [models](https://github.com/nahumsa/nyc-yellow-tripdata/tree/main/models): Where the following models are trained and evaludated:
    - Linear Regression
    - Random Forest
- [register](https://github.com/nahumsa/nyc-yellow-tripdata/tree/main/register): Where the model is registered to the MLFLOW model registry
- [notebooks](https://github.com/nahumsa/nyc-yellow-tripdata/tree/main/notebooks): Where exploratory notebooks are used before generating the modules
- [orchestration/prefect](https://github.com/nahumsa/nyc-yellow-tripdata/tree/main/orchestration/prefect): In this folder, there is the prefect orchestration to train the logistic regression model. This also has the deployment for the training logistic regression prefect flow.
- [scripts](https://github.com/nahumsa/nyc-yellow-tripdata/tree/main/scripts): Where there are scripts for the CI and initialization of MLFlow
- [tests](https://github.com/nahumsa/nyc-yellow-tripdata/tree/main/tests): Where there are tests for other modules

# MLOps Zoomcamp: Peer Review Criteria

* Problem description

    * [ ] 0 points: Problem is not described

    * [ ] 1 point: Problem is described but shortly or not clearly

    * [X] 2 points: Problem is well described and it's clear what the problem the project solves

* Cloud

    * [X] 0 points: Cloud is not used, things run only locally

    * [ ] 2 points: The project is developed on the cloud OR the project is deployed to Kubernetes or similar container management platforms

    * [ ] 4 points: The project is developed on the cloud and IaC tools are used for provisioning the infrastructure

* Experiment tracking and model registry

    * [ ] 0 points: No experiment tracking or model registry

    * [ ] 2 points: Experiments are tracked or models are registred in the registry

    * [X] 4 points: Both experiment tracking and model registry are used

* Workflow orchestration

    * [ ] 0 points: No workflow orchestration

    * [ ] 2 points: Basic workflow orchestration

    * [X] 4 points: Fully deployed workflow

* Model deployment

    * [ ] 0 points: Model is not deployed

    * [ ] 2 points: Model is deployed but only locally

    * [X] 4 points: The model deployment code is containerized and could be deployed to cloud or special tools for model deployment are used

* Model monitoring

    * [X] 0 points: No model monitoring

    * [ ] 2 points: Basic model monitoring that calculates and reports metrics

    * [ ] 4 points: Comprehensive model monitoring that send alerts or runs a conditional workflow (e.g. retraining, generating debugging dashboard, switching to a different model) if the defined metrics threshold is violated

* Reproducibility

    * [ ] 0 points: No instructions how to run code at all

    * [ ] 2 points: Some instructions are there, but they are not complete

    * [X] 4 points: Instructions are clear, it's easy to run the code, and the code works. The version for all the dependencies are specified.

* Best practices

    * [X] There are unit tests (1 point)

    * [ ] There is an integration test (1 point)

    * [X] Linter and/or code formatter are used (1 point)

    * [X] There's a Makefile (1 point)

    * [X] There are pre-commit hooks (1 point)

    * [X] There's a CI/CD pipeline (2 points)
