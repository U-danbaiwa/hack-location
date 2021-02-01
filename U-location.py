import requests, json
ip=input("Enter vuctim ip: ")
response ="https://app.abstractapi.com/json/"
re=requests.get(response+ip).json()
print(re["city"])
print(re["query"])
