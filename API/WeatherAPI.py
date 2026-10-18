from Service.WeatherAPIService import *
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_city_and_weather(city_name , city_id):
    city_weather = WeatherAPI_CurrentDayWeatherAPIDay(city_name=city_name , city_id=city_id)
    return city_weather