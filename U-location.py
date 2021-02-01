import requests
import json
ip=input("Enter vuctim ip: ")
response = requests.get("https://ipgeolocation.abstractapi.com/v1/?api_key=5df4ea3f9fbc4850b6fbc3fcdb19cf04&ip_address=",ip)
re=json.loads(response)
print(re["city"])
print(re[ip_address])
