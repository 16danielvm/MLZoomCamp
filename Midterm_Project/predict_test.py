import requests


url = 'http://localhost:9696/predict'

customer = {
    "snoring_rate": 93.80,
    "respiration_rate": 25.680,
    "body_temperature": 91.840,
    "limb_movement": 16.600,
    "blood_oxygen": 89.840,
    "eye_movement": 99.60,
    "sleeping_hours": 1.840,
    "heart_rate": 74.20
}
							
response = requests.post(url, json=customer).json() # .json() converts the response to JSON
print(response)

if response['stress_level'] == 0:
    print('Your stress level is low/normal.')
elif response['stress_level'] == 1:
    print('Your stress level is medium low.')
elif response['stress_level'] == 2:
    print('Your stress level is medium.')
elif response['stress_level'] == 3:
    print('Your stress level is medium high.')
elif response['stress_level'] == 4:
    print('Your stress level is high.')