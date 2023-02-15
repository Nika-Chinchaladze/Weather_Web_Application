import requests
import json
import os


class WeatherApi:
    def __init__(self):
        self.my_url = "http://api.weatherapi.com/v1/forecast.json?"

    def get_forecast(self, city):
        my_params = {
            "key": os.environ.get("MY_KEY"),
            "q": f"{city}",
            "days": "7",
            "aqi": "no",
            "alerts": "no"
        }

        respond = requests.get(self.my_url, params=my_params)
        data = respond.json()
        try:
            if data["location"]["name"] == city.capitalize():
                json_object = json.dumps(data, indent=4)
                with open("static/weather.json", "w") as file:
                    file.write(json_object)
                    file.close()
        except KeyError:
            pass
    
        return "DONE"

