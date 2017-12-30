from requests import get
import json
from pprint import pprint

url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/505307'

weather = get(url).json()['items']
pprint(weather)
