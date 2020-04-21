#!/usr/bin/env python
# coding: utf-8

# In[10]:


import requests


# In[18]:


def search_city(city):

    API_KEY = 'a070fcd8fc2db8d5d1f140466a2012b4'  # initialize your key here
    # call API and convert response into Python dictionary
    
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}'
    response = requests.get(url).json()


    # error like unknown city name, inavalid api key
    if response.get('cod') != 200:
        message = response.get('message', '')
        return f'Error getting temperature for {city.title()}. Error message = {message}'

    # get current temperature and convert it into Celsius
    current_temperature = response.get('main', {}).get('temp')
    if current_temperature:
        current_temperature_celsius = round(current_temperature - 273.15, 2)
        return f'Current temperature of {city.title()} is {current_temperature_celsius}'
    else:
        return f'Error getting temperature for {city.title()}'


# In[23]:


city = input("Enter city name:")
try: 
    for char in city:
        if char in "0123456789":
            raise ValueError
except ValueError:
    print ("Invalid city name")
    #exit()
else:
    print("city name %s" % city)
    result = search_city(city)
    print(result)


# In[22]:


result


# In[ ]:




