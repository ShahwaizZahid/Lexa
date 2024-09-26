import os
from dotenv import load_dotenv
import requests
load_dotenv()

weather_api_key = os.getenv('WEATHER_API_KEY')
def Weather(c):
    print(c)
    if "weather" in c.lower():
        try:
           
            city = c.lower().split(" ")[0]  # Fallback to the last word as city name
            
           
            url = f"http://api.weatherapi.com/v1/current.json?key={weather_api_key}&q={city}"
            r = requests.get(url)
            
            if r.status_code == 200:
                weather_data = r.json()
                temp_c = weather_data['current']['temp_c']
                condition = weather_data['current']['condition']['text']
                res = f"The weather in {city} is {temp_c} degrees Celsius with {condition}."
                return res
            else:
                res ="Sorry, I couldn't fetch the weather information. Please check the city name."
                return res
        except Exception as e:
                res =  f"An error occurred: {str(e)}"
                return res
    