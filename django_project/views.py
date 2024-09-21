import requests
from django.shortcuts import render
  

from django.shortcuts import render
from django.conf import settings

def weather_view(request):
    api_key = settings.API_KEY
    return render(request, 'templates/index.html', {'api_key': api_key})
