import urllib, json 
ip_address =raw_input('enter ip: ');
url = 'https://api.ipfind.com/?ip=' + ip_address; 
response = urllib.urlopen(url) 
data = json.loads(response.read()) 
print data
