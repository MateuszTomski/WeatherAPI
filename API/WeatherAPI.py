from Service.WeatherAPIService import *
from fastapi import FastAPI

app = FastAPI()

@app.get("/Weather/{city_name}/CurrentDay")
def get_current_city_and_weather(city_name: str , city_id: int):
    city = WeatherAPI_CurrentDayWeatherAPIDay(city_name=city_name , city_id=city_id)
    return city

@app.get("/Weather/{city_name}/TommorowDay")
def get_current_city_and_weather(city_name: str , city_id: int):
    city = WeatherAPI_TommorowDayWeatherAPIDay(city_name=city_name , city_id=city_id)
    return city

