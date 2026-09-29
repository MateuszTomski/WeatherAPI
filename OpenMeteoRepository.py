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
    def __init__(self, latitude: float, longitude: float, forecast_days: int = 7) -> WeatherResponse:
        base_url = f"https://api.open-meteo.com/v1/forecast?"
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "forecast_days": forecast_days,
            "daily": WeatherFormatParams.daily.value,
            "hourly": WeatherFormatParams.hourly.value,
            "current": WeatherFormatParams.current.value
        }
        data = requests.get(base_url, params)
        self.wynik = data.json()

    def get_city_weather_info(self):
        return WeatherResponse.model_validate(self.wynik)

# kielce = OpenMeteoGeo("Kielce").get_city_cordinates()
# kielce2 =  OpenMeteoWeather(kielce[0], kielce[1]).get_city_weather_info()
# print(kielce2)