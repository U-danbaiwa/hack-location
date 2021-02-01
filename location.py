import requests
me=input("enter ip: ")
Url=("https://ipgeolocation.abstractapi.com/v1/?api_key=5df4ea3f9fbc4850b6fbc3fcdb19cf04&ip_address=\n")
res=requests.get(Url+me)
print(res.status_code)
print(res.ip_address)
print(res.city)
print(res.city_geoname_id)
