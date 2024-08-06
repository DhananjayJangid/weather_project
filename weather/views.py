import weather
import requests
from django.shortcuts import render
from .forms import CityForm

def get_weather_data(city):
    api_key = '5dedd63854f602205c355de3c70861b8'  # Replace with your OpenWeatherMap API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    return response.json()

def home(request):
    weather_data = {}
    form = CityForm()

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            weather_data = get_weather_data(city)

    return render(request, 'weather/home.html', {'form': form, 'weather_data': weather_data})
