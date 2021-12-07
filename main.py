import os
import requests
from os.path import join, dirname
from dotenv import load_dotenv


END_POINT = "https://api.openweathermap.org/data/2.5/onecall"

ASH_LAT = 42.1946
ASH_LONG = -122.709480

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


api_key = os.environ.get('API_KEY')

ashland = {
    "lat": ASH_LAT,
    "lon": ASH_LONG,
    "exclude": "minutely,current,daily",
    "appid": api_key
}

response = requests.get(END_POINT, params=ashland)
response.raise_for_status()
weather_data = response.json()

print(weather_data)
