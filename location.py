import argparse
import requests, json
import sys
from sys import argv
import os
ip = input("enter your ip: ")

api = "http://ip-api.com/json/"

try:
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        a = lgreen+bold+"[$]"
        b = cyan+bold+"[$]"
        print (a, "[Victim]:", data['query'])
        print(red+"<--------------->"+red)
        print (b, "[ISP]:", data['isp'])
        print(red+"<--------------->"+red)
        print (a, "[Organisation]:", data['org'])
        print(red+"<--------------->"+red)
        print (b, "[City]:", data['city'])
        print(red+"<--------------->"+red)
        print (a, "[Region]:", data['region'])
        print(red+"<--------------->"+red)
        print (b, "[Longitude]:", data['lon'])
        print(red+"<--------------->"+red)
        print (a, "[Latitude]:", data['lat'])
        print(red+"<--------------->"+red)
        print (b, "[Time zone]:", data['timezone'])
        print(red+"<--------------->"+red)
        print (a, "[Zip code]:", data['zip'])
        print ("By "+yellow)
