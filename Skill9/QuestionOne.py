import requests,json
url="https://api.openweathermap.org/data/2.5/weather?"
city=input('Enter Your City Name : ')
zip_code=input('Enter your Zip Code : ')
api_key="2f11a34501741bd5400aad8bec118483"
new=url+"zip="+zip_code+",us&appid="+api_key
response=requests.get(new)
if(response.status_code==200):
   data=response.json()
   main=data['main']
   temperature = main['temp']
   humadity=main['humidity']
   pressure = main['pressure']
   report=data['weather']
   long=data['coord']
   sun=data['sys']
   wind=data['wind']
   print(f"------------------------")
   print(f'City : {city}')
   print(f"Country : {sun['country']}")
   print(f'Zip Code : {zip_code}')
   print(f'------------------------')
   print(f"Longitude : {long['lon']}")
   print(f"Latitude  : {long['lat']}")
   print(f"Temperature : {temperature}")
   print(f"Wind Speed : {wind['speed']}")
   print(f'Humidity : {humadity}')
   print(f"Pressure : {pressure}")
   print(f"Weather Report : {report[0]['description']}")
else:
   print("Error in the HTTP request")
#Alaska