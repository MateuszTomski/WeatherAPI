import requests
from model.OpenMeteoModel import *

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

    def get_city_list(self):
        return [WeatherGeoForAPI.model_validate(city) for city in self.wynik['results']]


        


class OpenMeteoWeather: 
    def __init__(self, latitude: float, longitude: float, forecast_days: int = 7) -> WeatherResponse:
        base_url = f"https://api.open-meteo.com/v1/forecast?"
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "forecast_days": forecast_days,
            "daily": WeatherRequestParams.daily.value,
            "hourly": WeatherRequestParams.hourly.value,
            "current": WeatherRequestParams.current.value
        }
        data = requests.get(base_url, params)
        self.wynik = data.json()
        self.wynik_model = WeatherResponse.model_validate(self.wynik)

    def get_city_weather_info(self):
        return self.wynik_model

    def get_current_weather(self):
        return self.wynik_model.current

    def get_hourly_weather(self):
        return self.wynik_model.hourly

    def get_daily_weather(self):
        return self.wynik_model.daily


# kielce1 = OpenMeteoGeo("kielce").get_city_cordinates()
# kielce = OpenMeteoWeather(latitude=kielce1[0], longitude=kielce1[1]).get_daily_weather()
# print(kielce)

# kielce = OpenMeteoGeo("Kielce").get_city_list()
# print(kielce)