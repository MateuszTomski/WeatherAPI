from OpenMeteoRepository import *

def current_weather(city_name: str):
    city = OpenMeteoGeo(city_name=city_name).get_city_cordinates()
    city_weather = OpenMeteoWeather(latitude=city[0], longitude=city[1]).get_city_info()

    return f"Obecna pogoda w {city_name}, Czas: {city_weather.current.time}, Temperatura: {city_weather.current.temperature_2m}, Deszcz {city_weather.current.rain}, Snieg {city_weather.current.snowfall}, Mrzawka {city_weather.current.showers}, Pogoda: {WeatherCode.get_values(city_weather.current.weather_code)}, Pora Dnia: {DayNight.get_values(city_weather.current.is_day)}"

def daily_weather(city_name: str):
    city = OpenMeteoGeo(city_name=city_name).get_city_cordinates()
    city_weather = OpenMeteoWeather(latitude=city[0], longitude=city[1]).get_city_info()

    return f"Pogoda na dzisiaj w {city_name}, Data: {city_weather.daily.time[0]}, Maksymalna Temperatura: {city_weather.daily.temperature_max[0]}, Najnizsza Temperatura {city_weather.daily.temperature_min[0]}, Pogoda: {WeatherCode.get_values(city_weather.daily.weather_code)}"

def get_five_days_weather(city_name: str):

    city = OpenMeteoGeo(city_name=city_name).get_city_cordinates()
    city_weather = OpenMeteoWeather(latitude=city[0], longitude=city[1]).get_city_info()

    daily = city_weather.daily

    return [
        WeatherDay(
            time=daily.time[i],
            temperature_max=daily.temperature_max[i],
            temperature_min=daily.temperature_min[i],
            weather_code=daily.weather_code[i]
        )
        for i in range(5)
    ]

def five_days_format(city_name : str):
    city_weather = get_five_days_weather(city_name)
    print(f"Pogoda w {city_name} na 5 kolejnych dni: ")
    for weather in city_weather:
        yield f"Date: {weather.time}, Maksymalna Temperatura: {weather.temperature_max}, Minimalna Temperatura: {weather.temperature_min}, Pogoda {WeatherCode.get_values(weather.weather_code)}"


    


    
