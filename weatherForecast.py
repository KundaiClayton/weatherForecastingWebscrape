# -*- coding: utf-8 -*-
"""
Created on Sat May 30 18:37:25 2020

@author: kundie

"""

import pandas as pd
import requests
from bs4 import BeautifulSoup

#url we are getting data from
url=requests.get('https://forecast.weather.gov/MapClick.php?lat=41.8843&lon=-87.6324#.XIRQYFNKgUE')

soup=BeautifulSoup(url.content,'html.parser')
week=soup.find(id='seven-day-forecast-body')

print(week)

items=week.find_all(class_='tombstone-container')
for i in range(len(items)):
    print(items[i])
print("***********")
print(items[0])
print(items[0].find(class_='period-name').get_text())
print(items[0].find(class_='short-desc').get_text().strip())
print(items[0].find(class_='temp temp-high').get_text())

#date=[item.find(class_='period-name').get_text() for item in items]

#date array contains the time of the day to forecast
dayOfWeek=[]

for item in items:
    time_of_day= item.find(class_='period-name').get_text() 
    dayOfWeek.append(time_of_day)

print(dayOfWeek)

##array which contains a short description of what the weather is like
short_descriptions =[]
for item in items:
    description=item.find(class_='short-desc').get_text()
    short_descriptions.append(description)

#array which contains temperatures

temperatures=[item.find(class_='temp').get_text() for item in items]
    
print(short_descriptions)

weather=pd.DataFrame(
    {
         'dayOfWeek':dayOfWeek,
         'description':short_descriptions,
         'temperature':temperatures
     }
    )

print(weather)