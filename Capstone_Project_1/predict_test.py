import requests


url = 'http://localhost:9696/predict'


#Assuming that the data has been encoded and scaled.
customer = {
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
}

response = requests.post(url, json=customer).json() # .json() converts the response to JSON
print(response)

if response['status'] == 0:
    print('Your Cirrhosis status is C.')
elif response['status'] == 1:
    print('Your Cirrhosis status is CL.')
elif response['status'] == 2:
    print('Your Cirrhosis status is D.')
