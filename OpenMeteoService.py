from OpenMeteoRepository import *

def get_weather(city_name: str, wheather_format: WeatherFormat):
    cordinates = OpenMeteoGeo(city_name=city_name).get_city_cordinates()
    city_weather = OpenMeteoWeather(latitude=cordinates[0], longitude=cordinates[1]).get_city_weather_info()

    if wheather_format == WeatherFormat.daily:
        return WeatherStringFormat.daily_weather_format(city_name, city_weather)
    elif wheather_format == wheather_format.current:
        return WeatherStringFormat.current_weather_format(city_name, city_weather)


def get_tommorows_weather(city_name : str):
    cordinates = OpenMeteoGeo(city_name=city_name).get_city_cordinates()
    city_weather = OpenMeteoWeather(latitude=cordinates[0], longitude=cordinates[1]).get_city_weather_info()

    return WeatherStringFormat.tommorow_weather_format(city_name , city_weather)

def get_days_weather(city_name: str, days: int = 7) -> list[WeatherDay]:

    cordinates = OpenMeteoGeo(city_name=city_name).get_city_cordinates()
    city_weather = OpenMeteoWeather(latitude=cordinates[0], longitude=cordinates[1]).get_city_weather_info()

    daily = city_weather.daily

    return [
        WeatherDay(
            time=daily.time[i],
            temperature_max=daily.temperature_max[i],
            temperature_min=daily.temperature_min[i],
            weather_code=daily.weather_code[i]
        )
        for i in range(days)
    ]

def get_weather_for_multiple_days(city_name: str , days: int = 3 ):
    list_days_weather = get_days_weather(city_name)
    return WeatherStringFormat.multiple_days_weather_format(city_name, days, list_days_weather)






    
