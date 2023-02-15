from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import weather_api, json_class, date_class

# create django form
from .forms import CityForm

# Create your views here.


def home_page(request):
    if request.method == "POST":
        control_form = CityForm(request.POST)
        if control_form.is_valid():
            weather_tool = weather_api.WeatherApi()
            weather_tool.get_forecast(
                city=control_form.cleaned_data["cityName"])
            generated_correct_url = reverse("home-page")
            return HttpResponseRedirect(generated_correct_url)

    form = CityForm()
    date_tool = date_class.ConvertDate()
    json_tool = json_class.JsonClass()
    request_date = json_tool.request_date()
    day_forecast = json_tool.days_forecast()
    hour_forecast = json_tool.hours_forecast(chosen_date=request_date)
    day_name = date_tool.get_weekday(enter_date=request_date)
    return render(request, "weather/index.html", {
        "forecast": day_forecast,
        "hour_cast": hour_forecast,
        "day_name": day_name,
        "form": form
    })


def chosen_page(request, manuscript):
    if request.method == "POST":
        control_form = CityForm(request.POST)
        if control_form.is_valid():
            weather_tool = weather_api.WeatherApi()
            weather_tool.get_forecast(
                city=control_form.cleaned_data["cityName"])
            generated_correct_url = reverse("home-page")
            return HttpResponseRedirect(generated_correct_url)

    form = CityForm()
    date_tool = date_class.ConvertDate()
    json_tool = json_class.JsonClass()
    day_forecast = json_tool.days_forecast()
    hour_forecast = json_tool.hours_forecast(chosen_date=manuscript)
    day_name = date_tool.get_weekday(enter_date=manuscript)
    return render(request, "weather/index.html", {
        "forecast": day_forecast,
        "hour_cast": hour_forecast,
        "day_name": day_name,
        "form": form
    })
