from requests import get
import matplotlib.pyplot as plt
from dateutil import parser

url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/505307'

weather = get(url).json()

## Use a for loop to iterate over the temperature and add to a list
temperatures = []
for record in weather['items']:
    temperature = record['ambient_temp']
    temperatures.append(temperature)

## list comprehension to get all the temperatures in a list
temperatures = [record['ambient_temp'] for record in weather['items']]

## list comprehension to get all the timestamps in a list
timestamps = [parser.parse(record['reading_timestamp']) for record in weather['items']]

## create a plot of timestamps against temperature and show it
plt.plot(timestamps, temperatures)
## Set the axis labels
plt.ylabel('Temperature')
plt.xlabel('Time')
plt.show()
