from dotenv import load_dotenv
from pprint import pprint
import requests
#to assist us to get the variables is the .env file
import os

load_dotenv()

#get the weather variables and get the city to search for the weather conditions
def getCurrentWeather(city="Lagos"):
    #the request url
    requestURL = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    #make the request and get the response
    weatherData = requests.get(requestURL).json()
    #return the weather data
    return weatherData
#make it a module
if __name__ == '__main__':
    #this will show on the terminal if the file is called directly
    print("\n*** Get Current Weather Conditions ***\n")
    city = input("\n Please enter a city name: ")
    #we need to make sure the city input is not an empty string or string with only spaces
    if not bool(city.strip()):
        city = "Lagos"
    #then we need to get the data for the city by calling the function and passing the city as the argument
    weatherData = getCurrentWeather(city)
    #print the weather data
    pprint(weatherData)

