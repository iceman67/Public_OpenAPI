import requests
from bs4 import BeautifulSoup

def search_city(city):

    API_KEY = 'a070fcd8fc2db8d5d1f140466a2012b4'  # initialize your key here
    # call API and convert response into Python dictionary
    
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}&mode=xml'
    #print (url)
    response = requests.get(url)
    # error like unknown city name, inavalid api key
    if response.status_code != 200:
        message = response.get('message', '')
        return f'Error getting temperature for {city.title()}. Error message = {message}'

    content = response.content
    soup = BeautifulSoup(content, "xml")
    
     # get current temperature and convert it into Celsius
    current_temperature = soup.find('temperature')['value']  
 
    if current_temperature:
        current_temperature_celsius = round(float(current_temperature) - 273.15, 2)
        return f'Current temperature of {city.title()} is {current_temperature_celsius}'
    else:
        return f'Error getting temperature for {city.title()}'

result = search_city('Seoul')
print(result)
