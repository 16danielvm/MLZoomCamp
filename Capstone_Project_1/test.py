import requests

url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

# url = 'https://zoiz6i4tu8.execute-api.us-east-2.amazonaws.com/test/predict'

data = {'customer' : {
    "Bilirubin": -0.707522,
    "Copper": 0.799566,
    "N_Days": -0.261788,
    "Stage": 2,
    "Hepatomegaly": 0,
    "Prothrombin": -1.224804,
    "SGOT": -0.913350,
    "Edema": 0,
    "Platelets": 0.568196,
    "Age": 1.336986,
    "Cholesterol": -1.178809,
    "Drug": 1
}}

result = requests.post(url, json=data).json()
print(result)