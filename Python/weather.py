from requests import get
import json

url = 'https://api.weather.gov'

weather = get(url).json()

print(weather)

print(weather['status'])
