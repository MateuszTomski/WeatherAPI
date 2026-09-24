from OpenMeteoRepository import *

def get_weather(city_name: str, wheather_format: WeatherFormat):
    cordinates = OpenMeteoGeo(city_name=city_name).get_city_cordinates()
    city_weather = OpenMeteoWeather(latitude=cordinates[0], longitude=cordinates[1]).get_city_weather_info()

    if wheather_format == WeatherFormat.daily:
        return WeatherStringFormat.daily_weather_format(city_name, city_weather)
    elif wheather_format == wheather_format.current:
        return WeatherStringFormat.current_weather_format(city_name, city_weather)

def get_days_weather(city_name: str, days: int = 5):

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

def days_format(city_name : str):
    city_weather = get_days_weather(city_name)
    print(f"Pogoda w {city_name} na 5 kolejnych dni: ")
    for weather in city_weather:
        yield f"Data: {weather.time}, Maksymalna Temperatura: {weather.temperature_max}, Minimalna Temperatura: {weather.temperature_min}, Pogoda {WeatherCode.get_values(weather.weather_code)}"


    


    
