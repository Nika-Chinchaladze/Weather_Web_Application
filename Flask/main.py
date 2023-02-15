from flask import Flask, render_template, redirect, url_for, request
from weather_api import WeatherApi
from json_class import JsonClass
from date_class import ConvertDate

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home_page():
    if request.method == "POST":
        result = WeatherApi()
        result.get_forecast(city=request.form.get("city"))
        return redirect(url_for("home_page"))
    tool_1 = JsonClass()
    tool_2 = ConvertDate()
    request_date = tool_1.request_date()
    days_data = tool_1.days_forecast()
    hours_data = tool_1.hours_forecast(chosen_date=request_date)
    chosen_day = tool_2.get_weekday(enter_date=request_date)
    return render_template("index.html", data=days_data, hour_data=hours_data, chosen_day=chosen_day)


@app.route("/<string:chosen_date>", methods=["GET", "POST"])
def chosen_page(chosen_date):
    if request.method == "POST":
        result = WeatherApi()
        result.get_forecast(city=request.form.get("city"))
        return redirect(url_for("home_page"))
    tool_1 = JsonClass()
    tool_2 = ConvertDate()
    days_data = tool_1.days_forecast()
    hours_data = tool_1.hours_forecast(chosen_date=chosen_date)
    chosen_day = tool_2.get_weekday(enter_date=chosen_date)
    return render_template("index.html", data=days_data, hour_data=hours_data, chosen_day=chosen_day)


if __name__ == "__main__":
    app.run(debug=True)
