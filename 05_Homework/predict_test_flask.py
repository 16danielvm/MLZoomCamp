import requests

url = "http://localhost:9696/predict_flask"
client = {"job": "unknown", "duration": 270, "poutcome": "failure"}
response = requests.post(url, json=client).json()

print(response)