import requests
import os
from requests.auth import HTTPBasicAuth
import json


#yup = requests.get('https://api.planningcenteronline.com/people/v2', auth=('947f0f7e737cb7846eb65850d0eed067b4eed0786b055694a9d2a7a6a27e5e39', ''))
#print(yup)
api_key = "952221b0e8982da6cab70ce63e6194a5a16cac1c9b5f7402a0f096921f41f48a"
api_secret = "1100e80506d88589527cbd41c28dfb9c0e6009bb9718174870ac6448209cd54f"

# Create Base64 Encoded Basic Auth Header
auth = HTTPBasicAuth(api_key, api_secret)

headers = {
'Authorization': 'Basic ' + api_key,
'Content-Type': 'application/json'
}

limit = 1000
params = {"limit": limit}
#json_practice ={"url": "https://q0i6ebd0cj.execute-api.us-east-1.amazonaws.com/prod/fivetran_webhooks", "events": ["status"], "active": True}
#api url
url = 'https://api.planningcenteronline.com/services/v2'


#this is used to create the json object and the data needed exists in the data->items key pairs
response = requests.get(url=url, auth=auth, params=params).json()
#fun_stuff = response['data']
#fun_fun_stuff = r['attributes']['name']
'''
for _ in fun_stuff: 

    print('++++++++++++++++++++++++++++++++++++++++++++++')
    print(_)
    print('++++++++++++++++++++++++++++++++++++++++++++++')
'''
print(response)