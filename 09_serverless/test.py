import requests

# url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

url = 'https://zoiz6i4tu8.execute-api.us-east-2.amazonaws.com/test/predict'

data = {'url': 'http://bit.ly/mlbookcamp-pants'}

result = requests.post(url, json=data).json()
print(result)