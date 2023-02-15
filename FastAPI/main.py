from fastapi import FastAPI, Request, status, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from date_class import ConvertDate
from json_class import JsonClass
from weather_api import WeatherApi

app = FastAPI()

# DIRECTORY FOR => Templates and Static Files:
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")



@app.get("/")
def index_page(request: Request):
    date_tool = ConvertDate()
    json_tool = JsonClass()
    last_date = json_tool.request_date()
    day_forecast = json_tool.days_forecast()
    hour_forecast = json_tool.hours_forecast(chosen_date=last_date)
    current_day = date_tool.get_weekday(enter_date=last_date)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "day_data": day_forecast,
        "hour_data": hour_forecast,
        "day_name": current_day
    })



@app.post("/search")
def index_post_page(request: Request, cityName: str = Form(...)):
    api_tool = WeatherApi()
    api_tool.get_forecast(city=cityName)
    redirect_url = app.url_path_for("index_page")
    return RedirectResponse(url=f'{redirect_url}', status_code=status.HTTP_303_SEE_OTHER)


@app.get("/date/{chosen_date}")
def chosen_page(request: Request, chosen_date):
    date_tool = ConvertDate()
    json_tool = JsonClass()
    day_forecast = json_tool.days_forecast()
    hour_forecast = json_tool.hours_forecast(chosen_date=chosen_date)
    current_day = date_tool.get_weekday(enter_date=chosen_date)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "day_data": day_forecast,
        "hour_data": hour_forecast,
        "day_name": current_day
    })
