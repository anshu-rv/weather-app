from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    city=request.GET.get("city","bengaluru")
    api_url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=b87770e0c526050cc7426cd23fa9cf28&units=metric"
    
    api=requests.get(api_url).json()
    temperature=api['main']['temp']
    country=api['sys']['country']
    city_name=api["name"]
    humidity=api['main']['humidity']
    speed = api['wind']['speed']
    weather=api['weather'][0]['description']
    cloud=api['weather'][0]['main']
    icon = api['weather'][0]['icon']
    icon_url = f'https://openweathermap.org/img/wn/{icon}@2x.png'
    return render(request,"index.html",{'temperature':temperature,"country":country,"city":city_name,"humidity":humidity,"weather":weather,"cloud":cloud, 'speed':speed, 'icon':icon_url})
