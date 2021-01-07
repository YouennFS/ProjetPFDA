import requests
import json

url = 'http://0.0.0.0:5000/api/'

data = [[0, 254, 0, -5.2, 37, 2.2, 2000, -17.6, 0.0, 0.0, 0.0, 0, 0,1,0,0,0,0,12]]
j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print(r, r.text)
