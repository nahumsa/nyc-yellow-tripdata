# Predicting the time for the NYC yellow taxi trip

In this project, the goal is to predict the time based on the yellow taxi pickup and dropoff location, and other additional features.

# How to run the code

## Folder structure

In this project, there are the following folders:

- [etl](https://github.com/nahumsa/nyc-yellow-tripdata/tree/main/etl): Which is responsible for data preprocessing and loading.
- [data](https://github.com/nahumsa/nyc-yellow-tripdata/tree/main/data): Where the data is stored
- [models](https://github.com/nahumsa/nyc-yellow-tripdata/tree/main/models): Where the following models are trained and evaludated:
    - Linear Regression
    - Random Forest
- [notebooks](https://github.com/nahumsa/nyc-yellow-tripdata/tree/main/notebooks): Where exploratory notebooks are used before generating the modules
- [scripts](https://github.com/nahumsa/nyc-yellow-tripdata/tree/main/scripts): Where there are scripts for the CI and initialization of MLFlow
- [tests](https://github.com/nahumsa/nyc-yellow-tripdata/tree/main/tests): Where there are tests for other modules

# Peer Review Criteria

* Problem description

    * [ ] 0 points: Problem is not described

    * [X] 1 point: Problem is described but shortly or not clearly 

    * [ ] 2 points: Problem is well described and it's clear what the problem the project solves

* Cloud

    * [X] 0 points: Cloud is not used, things run only locally

    * [ ] 2 points: The project is developed on the cloud OR the project is deployed to Kubernetes or similar container management platforms

    * [ ] 4 points: The project is developed on the cloud and IaC tools are used for provisioning the infrastructure

* Experiment tracking and model registry

    * [ ] 0 points: No experiment tracking or model registry

    * [X] 2 points: Experiments are tracked or models are registred in the registry

    * [ ] 4 points: Both experiment tracking and model registry are used

* Workflow orchestration

    * [X] 0 points: No workflow orchestration

    * [ ] 2 points: Basic workflow orchestration

    * [ ] 4 points: Fully deployed workflow 

* Model deployment

    * [X] 0 points: Model is not deployed

    * [ ] 2 points: Model is deployed but only locally

    * [ ] 4 points: The model deployment code is containerized and could be deployed to cloud or special tools for model deployment are used

* Model monitoring

    * [X] 0 points: No model monitoring

    * [ ] 2 points: Basic model monitoring that calculates and reports metrics

    * [ ] 4 points: Comprehensive model monitoring that send alerts or runs a conditional workflow (e.g. retraining, generating debugging dashboard, switching to a different model) if the defined metrics threshold is violated

* Reproducibility

    * [X] 0 points: No instructions how to run code at all

    * [ ] 2 points: Some instructions are there, but they are not complete

    * [ ] 4 points: Instructions are clear, it's easy to run the code, and the code works. The version for all the dependencies are specified.

* Best practices

    * [ ] There are unit tests (1 point)

    * [ ] There is an integration test (1 point)

    * [X] Linter and/or code formatter are used (1 point)

    * [ ] There's a Makefile (1 point)

    * [ ] There are pre-commit hooks (1 point)

    * [X] There's a CI/CD pipeline (2 points)

