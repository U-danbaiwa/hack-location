import requests, json
ip=input("Enter vuctim ip: ")
response ="http://ip-api.com/json/"
re=requests.get(response+ip).json()
print(re["city"])
print(re["query"])
