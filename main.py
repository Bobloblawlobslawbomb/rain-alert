import os
from os.path import join, dirname
import requests
from twilio.rest import Client
from dotenv import load_dotenv


END_POINT = "https://api.openweathermap.org/data/2.5/onecall"

ASH_LAT = 42.1946
ASH_LONG = -122.709480

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


api_key = os.environ.get('API_KEY')
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
phone_to = os.environ.get('PHONE_TO')
phone_from = os.environ.get('PHONE_FROM')


ashland = {
    "lat": ASH_LAT,
    "lon": ASH_LONG,
    "exclude": "minutely,current,daily",
    "appid": api_key
}

response = requests.get(END_POINT, params=ashland)
response.raise_for_status()
weather_data = response.json()

half_day = weather_data["hourly"][:12]

will_it_rain = False

for hour_data in half_day:
    code = int(hour_data["weather"][0]["id"])
    if code < 700:
        will_rain = True

if will_it_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="It's going to rain today. Bring an umbrella.",
                        from_=phone_from,
                        to=phone_to
                    )
    print(message.status)
