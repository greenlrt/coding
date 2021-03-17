from requests import get
##import json

url = 'https://www1.ncdc.noaa.gov'

noaa = get(url)

print(noaa)
