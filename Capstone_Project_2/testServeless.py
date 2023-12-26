import requests

url = 'https://hvr312vdj8.execute-api.us-east-2.amazonaws.com/test_mask/predict'

data = {'url': 'https://raw.githubusercontent.com/16danielvm/MLZoomCamp/master/Capstone_Project_2/final_model/45.png'}

result = requests.post(url, json=data).json()
print(result)
print('------------------')
if result['WithMask'] > result['WithoutMask']:
    print('Relax! This person is wearing a mask')
else:
    print('ALERT! This person is not wearing a mask')