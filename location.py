import requests
ip=input("Enter ip: ")
response = requests.get("https://ipgeolocation.abstractapi.com/v1/?api_key=5df4ea3f9fbc4850b6fbc3fcdb19cf04&ip_address="+ip)
print(response.status_code)
print(response.content)
