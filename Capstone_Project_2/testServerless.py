import requests

url = 'https://hvr312vdj8.execute-api.us-east-2.amazonaws.com/test_mask/predict'

data = {'url': 'https://www.osfhealthcare.org/blog/wp-content/uploads/2020/10/business-woman-wearing-a-mask-f1.jpg'}

result = requests.post(url, json=data).json()
print(result)
print('------------------')
if result['WithMask'] > result['WithoutMask']:
    print('Relax! This person is wearing a mask')
else:
    print('ALERT! This person is not wearing a mask')