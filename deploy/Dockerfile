FROM python:3.8.14-slim

RUN pip install -U pip
RUN pip install pipenv
WORKDIR /app

COPY [ "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY [ "load.py", "load.py"]
COPY [ "serve_script.py", "serve_script.py"]

ENTRYPOINT ["python", "batch_script.py"]
