import requests 
import json 
# Your API key, available from your account page 
YOUR_GEOLOCATION_KEY=input('ENTER VICTIM IP')
# URL to send the request to 
request_url = 'https://ipgeolocation.abstractapi.com/v1/?api_key=' + YOUR_GEOLOCATION_KEY 
response = requests.get(request_url)
result = json.loads(response.content) 
print(result) 
print('ip_address: {}'.format(result['ip_address']))
