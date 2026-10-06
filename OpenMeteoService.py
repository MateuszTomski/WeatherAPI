from OpenMeteoRepository import *
from model.OpenMeteoModel import *

def get_weather_for_city(city_name: str):
    city_coridantes = OpenMeteoGeo(city_name=city_name).get_city_cordinates()
    city_weather = OpenMeteoWeather(latitude=city_coridantes[0], longitude=city_coridantes[1]).get_city_weather_info()
    country_code = city_coridantes[2]

    return city_weather, country_code

def get_weather_object(city_name: str, weather_format: WeatherFormat):
    city_cordinates = OpenMeteoGeo(city_name).get_city_cordinates()
    
    
    if weather_format == WeatherFormat.daily:
        weather_object_daily = OpenMeteoWeather(latitude=city_cordinates[0], longitude=city_cordinates[1])
        return weather_object_daily.wynik
    elif weather_format == WeatherFormat.hourly:
        weather_object_hourly = OpenMeteoWeather(latitude=city_cordinates[0], longitude=city_cordinates[1]).get_hourly_weather()
        return weather_object_hourly
    elif weather_format == WeatherFormat.current:
        weather_object_current = OpenMeteoWeather(latitude=city_cordinates[0], longitude=city_cordinates[1]).get_current_weather()
        return weather_object_current



def get_weather_for_tommorow(city_name: str, weather_format: WeatherFormat):
    city_weather, _ = get_weather_for_city(city_name)
    weather_for_city_tommorow = WeatherDay.convert(weather_response=city_weather, day=1)
    return weather_for_city_tommorow





def get_weather_for_days():
    pass

def get_compared_weather():
    pass

print(get_weather_for_tommorow("Wroclaw", weather_format=WeatherFormat.daily))


