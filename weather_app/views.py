from django.shortcuts import render, redirect
import requests
from pprint import pprint


link = 'https://api.openweathermap.org/data/2.5/weather'

def index(request):
    return render(request, 'index.html')
    
def get_city(request):
    city = request.POST['city']
    request.session['city'] = city
    return redirect('/get_weather')

def get_weather(request):
    parameters = {
        'q':request.session['city'],
        'appid': 'ca9d998adbcd7f78991be5204dd8d5d6'
    }
    weather_link = requests.get(link, params=parameters).json()
    weather_link = pprint(weather_link)
    
    context = {
        'weather_link': weather_link
    }
    return render(request, 'show_weather.html', context)

    


# Create your views here.
