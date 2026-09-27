import requests
from model import *

class OpenMeteoGeo:
    def __init__(self,city_name: str, count: int =10, language: str="en"):
        base_url = f"https://geocoding-api.open-meteo.com/v1/search?"
        params = {"name": city_name,
                  "count": count,
                  "language": language,
                  "format": "json"}
        data = requests.get(base_url, params)
        self.wynik = data.json()


    def get_city_info_list(self) -> list[WeatherGeoList]:
        return[WeatherGeoList.model_validate(city) for city in self.wynik['results']]


    def get_city_cordinates(self):
        city_info = [WeatherGeo.model_validate(city) for city in self.wynik['results']]
        for info in city_info:
            return info.latitude, info.latitude, info.country_code



        


class OpenMeteoWeather: 
    def __init__(self, latitude: float, longitude: float) -> Weather:
        base_url = f"https://api.open-meteo.com/v1/forecast?"
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "daily": ["temperature_2m_max", "temperature_2m_min", "weather_code"],
            "hourly": ["temperature_2m", "rain", "weather_code", "wind_speed_10m", "snowfall", "showers"],
            "current": ["temperature_2m","rain","snowfall","showers","weather_code","wind_speed_10m","is_day"]
        }
        data = requests.get(base_url, params)
        self.wynik = data.json()

    def get_city_weather_info(self):
        return Weather.model_validate(self.wynik)

