import requests, json
import os
import sys
#Colours that i will use
red = '\033[31m'
yellow = '\033[93m'
green = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'
cy='\033[095m'
cya='\033[035m'
os.system("clear")
os.system(cyan+"figlet U-danbaiwa")
print(cy+"\t\t\tv 1.0.0")
print("")
print("1:- IP INFORMATION")
print("2:- UPDATE TOOL")
print("")
for i in range(90):
	com=input("Enter Choice: ")
	if com=="1":
		os.system("clear")
		os.system(cyan+"figlet IP-INFO...")
		print(green+"\t\t\tv 1.0.0")
		print(cya+"\t\t   coded By U-danbaiwa")
		print("")
		print("")
		ip=input(green+bold+"[*] Enter Victim Ip:  ")
		response ="http://ip-api.com/json/"
		re=requests.get(response+ip).json()
		print("")
		print("")
		print(yellow+bold+"*************************VICTIM INFORMATION*************************")
		print(red+"[ * ] Victim ip:<=====>",re["query"])
		print(cyan+"[ * ] Status Code:<=====>",re["status"])
		print(green+"[ * ] Victim Continent:<=====>",re["continent"])
		print(cy+"[ * ] Victim Country:<=====>",re["country"])
		print(cya+"[ * ] Victim Country_Code:<=====>",re['countryCode'])
		print(cyan+"[ * ] Victim Region:<=====>",re["region"])
		print(green+"[ * ] Victim RegionName:<=====>",re["regionName"])
		print(cy+"[ * ] Victim City:<=====>",re["city"])
		print(cya+"[ * ] Latitude:<=====>",re["lat"])
		print(cy+"[ * ] Longitude:<=====>",re["lon"])
		print(red+"[ * ] Victim TimeZone:<=====>",re["timezone"])
		print(green+"[ * ] Victim Currency:<=====>",re["currency"])
		print(cyan+"[ * ] Victim Isp:<=====>",re["isp"])
		print(cy+"[ * ] Victim Org:<=====>",re["org"])
		print(cya+"[ * ] Victim As:<=====",re["as"])
		print(green+"[ * ] Victim Is Mobile:<=====>",re["mobile"])
		print(red+"[ * ] Victim Geo<=====>",["geo"])
		print("\n\n\t\t\tSHARE AND FOLLOW US FOR MORE TOOLS")
	elif com=="2":
	    os.system("clear")
        os.system(green+"figlet U-danbaiwa")
        print("please wait...")
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/U-danbaiwa/U-location.git")
        os.system("cd /data/data/com.termux/files/home")
        print("=====COMPLETE INSTALL THANK YOU=====")
	else:
		print("invalid command!")