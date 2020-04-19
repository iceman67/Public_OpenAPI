import requests


# https://code-maven.com/openweathermap-api-using-python
#https://stackoverflow.com/questions/46992156/parsing-data-in-dictionary-json-using-openweathermap-api
def search_city(city):

    API_KEY = 'a070fcd8fc2db8d5d1f140466a2012b4'  # initialize your key here
    # call API and convert response into Python dictionary

 
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}'
    response = requests.get(url).json()


    # error like unknown city name, inavalid api key
    if response.get('cod') != 200:
        message = response.get('message', '')
        return f'Error getting temperature for {city.title()}. Error message = {message}'


    description = response['weather'][0]['description']
    print( f'Current weather description of {city.title()} is {description}') 


    pressure = response['main']['pressure']
    print( f'Current pressure of {city.title()} is {pressure}') 


    current_humidity = response.get('main', {}).get('humidity')
    if current_humidity:
        print( f'Current humidity of {city.title()} is {current_humidity}')
    else:
        print( f'Error getting humidity for {city.title()}')
    
    # get current temperature and convert it into Celsius
    # city.title() Make the first letter in each word upper case
    current_temperature = response.get('main', {}).get('temp')
    if current_temperature:
        current_temperature_celsius = round(current_temperature - 273.15, 2)
        return f'Current temperature of {city.title()} is {current_temperature_celsius}'
    else:
        return f'Error getting temperature for {city.title()}'

   


while True:
    print("도시이름을 입력해 주세요")
    city = input()
    if city == 'Nocity':
        break
    result = search_city(city)
    print(result)




