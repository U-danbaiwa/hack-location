import requests, json
me=input("enter your ip: ")
response = requests.get("https://ipgeolocation.abstractapi.com/v1/?api_key=5df4ea3f9fbc4850b6fbc3fcdb19cf04&ip_address=",me).json()
print(response.status_code)
print(response.city)
print(response.city_geoname_id)
