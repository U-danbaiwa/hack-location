
import requests, json
import os
import sys
import time 
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
os.system("figlet U-danbaiwa")
print(cy+"\t\t\tv 1.1.0")
print("")
print(yellow+bold+"[1]IP INFORMATION")
print("")
print(green+bold+"[2]UPDATE TOOL")
print("")
for i in range(90):
	com=input("Enter Choice: ")
	if com=="1":
	  try:
		  os.system("clear")
		  os.system("figlet IP-INFO...")
	  	print(green+"\t\t\tv 1.1.0")
	  	print(cya+"\t\t   coded By U-danbaiwa")
  		print("")
		  print("")
	  	ip=input(green+bold+"[*] Enter Victim Ip:  ")
		
		  response ="http://ip-api.com/json/"
	  	re=requests.get(response+ip).json()
		  print("")
		  print("")
		  print(yellow+bold+"**********************VICTIM INFORMATION*******************")
	  	print("")
  		print(red+"[ * ] Victim ip:<=====>",re["query"])
	  	time.sleep(3)
	  	print("")
	  	print(cyan+"[ * ] Status Code:<=====>",re["status"])
	  	time.sleep(3)
	  	print("")
	  	print(cy+"[ * ] Victim Country:<=====>",re["country"])
	  	time.sleep(3)
		  print("")
	  	print(cya+"[ * ] Victim Country_Code:<=====>",re['countryCode'])
	  	time.sleep(3)
		  print("")
	  	print(cyan+"[ * ] Victim Region:<=====>",re["region"])
	  	time.sleep(3)
	  	print("")
	  	print(green+"[ * ] Victim RegionName:<=====>",re["regionName"])
	  	time.sleep(3)
		
	  	print("")
	  	print(cy+"[ * ] Victim City:<=====>",re["city"])
	  	time.sleep(3)
		  print("")
		  print(green+"[ * ] Latitude:<=====>",re["lat"])
	  	time.sleep(3)
		  print("")
	  	print(cy+"[ * ] Longitude:<=====>",re["lon"])
	  	time.sleep(3)
	  	print("")
		  print(red+"[ * ] Victim TimeZone:<=====>",re["timezone"])
	  	time.sleep(3)
	  	print("")
		  print(cyan+"[ * ] Victim Isp:<=====>",re["isp"])
	  	time.sleep(3)
	  	print("")
	  	print(cy+"[ * ] Victim Org:<=====>",re["org"])
		  time.sleep(3)
	  	print("")
	  	print(cya+"[ * ] Victim As:<=====",re["as"])
	  	time.sleep(3)
		  print("")
	  	print(green+"[ * ] Victim Zip Code:<=====>",re["zip"])
	  	time.sleep(3)
	  	print("")
	  	print(red+"[ * ] Victim Messega<=====>",["message"])
	  	time.sleep(3)
	  	print("")
		  print(red+"\n\n\tSHARE AND FOLLOW US FOR MORE TOOLS")
		  print("")
	except Exception:
		DB=("WRONG IP ADDRESS")
		print(green+bold" ".join(DB))
	elif com=="2":
	       os.system("clear")
	       os.system("figlet U-danbaiwa")
	       print("please wait...")
	       time.sleep(5)
	       os.system("cd /data/data/com.termux/files/home")
	       os.system("ls && rm -rf hack-location")
	       os.system("pkg update -y")
	       os.system("pkg install -y git")
	       os.system("pkg install python")
	       os.system("cd /data/data/com.termux/files/home && git clone https://github.com/U-danbaiwa/hack-location.git")
	     #ff7900
	       os.system("cd /data/data/com.termux/files/home")
	       print("\n")
	       print(red+"\t=====COMPLETE INSTALL THANK YOU=====")
	else:
		print("invalid command!")
