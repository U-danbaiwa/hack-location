import requests

response = requests.get("https://ipgeolocation.abstractapi.com/v1/?api_key=5df4ea3f9fbc4850b6fbc3fcdb19cf04&ip_address=197.210.174.187")
print(response.status_code)
#print(response.content)
