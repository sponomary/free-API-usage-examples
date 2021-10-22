import requests
from twilio.rest import Client


# OpenWeather One Call free API: https://openweathermap.org/
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "{your_OWM_api_key}"

# Get your coordinates: https://www.latlong.net/
# Note: here for Paris, France
longitude = 2.352222
latitude = 48.856613

weather_params = {
    "lat": latitude,
    "lon": longitude,
    "exclude": "current,minutely,daily",
    "appid": API_KEY
}

# Twilio API (sending SMS): https://www.twilio.com/
ACCOUNT_SID = "{your_account_id}"
AUTH_TOKEN = "{your_twilio_token}"
sender = "{from_number}"
addressee = "{to_number}"


response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
timezone = weather_data["timezone"]
weather_slice = weather_data["hourly"][:12]
weather_code = weather_data["hourly"][0]["weather"][0]["id"]
weather_description = weather_data["hourly"][0]["weather"][0]["description"]
print(f'La météo ({timezone}) : "{weather_description}" (code {weather_code}).')

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    # See the weather condition codes: https://openweathermap.org/weather-conditions
    if int(condition_code) < 600:  # codes corresponding to raining weather
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
                                  body="Aujourd'hui, il va pleuvoir ☔ ️: prends ton parapluie !",
                                  from_=sender,
                                  to=addressee
                              )
    print(f'Statut du message : "{message.status}".')
else:
    print("Bonne nouvelle : pas de pluie aujourd'hui !")
