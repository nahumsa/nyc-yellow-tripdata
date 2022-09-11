import requests

ride = {
    "PULocationID": 116,
    "DOLocationID": 238,
}

URL = "http://localhost:8000/predict"
response = requests.post(URL, json=ride)
print(response.json())
