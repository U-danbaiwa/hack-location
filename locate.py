import json
import requests

# Your API key, available from your account page
YOUR_GEOLOCATION_KEY = "https://ipgeolocation.abstractapi.com/v1/?api_key=5df4ea3f9fbc4850b6fbc3fcdb19cf04&ip_address=197.210.63.102"

# IP addretest
ip_address =input("Enter ip: ")

request_url = 'https://ipgeolocation.abstractapi.com/v1/?api_key=' + YOUR_GEOLOCATION_KEY + '&ip_address=' + ip_address
result = json.loads(response.content)
print(result)
