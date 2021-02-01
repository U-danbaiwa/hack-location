import re
import json
from urllib2 import urlopen
Me=input("enter ip: ")
url = 'http://ipinfo.io/json'
response = urlopen(url+Me)
data = json.load(response)

IP=(data['ip'])
org=(data['org'])
city =(data['city'])
country=(data['country'])
region=(data['region'])

print('Your IP detail')
print(IP)
print(org)
print(city)
print(country)
print(region)
