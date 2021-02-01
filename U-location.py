import requests
import json
ip=input("Enter vuctim ip: ")
response ="http://ip-api.com/json/"
res=requests.get(response+ip)
re=json.loads(res)
print(re["city"])
print(re["query"])
