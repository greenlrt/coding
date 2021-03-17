from requests import get
import json

url = 'https://opensky-network.org/api/states/all'

flights = get(url).json()

print(flights)
