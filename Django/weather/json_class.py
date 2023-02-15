import json


class JsonClass:
    def __init__(self):
        self.my_file = "static/weather.json"

    def read_json(self):
        with open(self.my_file, "r") as file:
            data = json.load(file)
            file.close()
            return data

    def request_date(self):
        data = self.read_json()["location"]["localtime"]
        answer = data.split()[0]
        return answer

    def days_forecast(self):
        data = self.read_json()
        day_forecast = []
        for item in data["forecast"]["forecastday"]:
            day_forecast.append({
                "day_date": item["date"],
                "day_temp": item["day"]["avgtemp_c"],
                "day_icon": f'https:{item["day"]["condition"]["icon"]}',
                "day_text": item["day"]["condition"]["text"]
            })

        answer = {
            "city": data["location"]["name"],
            "country": data["location"]["country"],
            "temp_c": data["current"]["temp_c"],
            "description": data["current"]["condition"]["text"],
            "icon": f'https:{data["current"]["condition"]["icon"]}',
            "days": day_forecast
        }
        return answer

    def hours_forecast(self, chosen_date):
        data = self.read_json()
        hours = data["forecast"]["forecastday"]
        result = next(item for item in hours if item["date"] == chosen_date)
        answer = []
        for item in result["hour"]:
            answer.append({
                "time": item["time"],
                "temp_c": item["temp_c"],
                "description": item["condition"]["text"],
                "icon": f'https:{item["condition"]["icon"]}'
            })
        return answer

