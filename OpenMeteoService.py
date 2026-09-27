from OpenMeteoRepository import *

def get_weather(city_name: str, wheather_format: WeatherFormat):
    cordinates = OpenMeteoGeo(city_name=city_name).get_city_cordinates()
    city_weather = OpenMeteoWeather(latitude=cordinates[0], longitude=cordinates[1]).get_city_weather_info()
    country_code = cordinates[2]
    
    
    if wheather_format == wheather_format.daily:
        return WeatherStringFormat.daily_weather_format(city_name, city_weather, country_code)
    elif wheather_format == wheather_format.current:
        return WeatherStringFormat.current_weather_format(city_name, city_weather, country_code)


def get_tommorows_weather(city_name : str):
    cordinates = OpenMeteoGeo(city_name=city_name).get_city_cordinates()
    city_weather = OpenMeteoWeather(latitude=cordinates[0], longitude=cordinates[1]).get_city_weather_info()
    country_code = cordinates[2]

    return WeatherStringFormat.tommorow_weather_format(city_name , city_weather, country_code)

def compare_weather(city_name: str, second_city_name: str, day: int = 0):
    cordinates_city_one = OpenMeteoGeo(city_name=city_name).get_city_cordinates()
    weather_for_city_one = OpenMeteoWeather(latitude=cordinates_city_one[0], longitude=cordinates_city_one[1]).get_city_weather_info()
    country_code_city_one = cordinates_city_one[2]
    avarage_temperature_city_one = weather_for_city_one.daily.temperature_min[day] + weather_for_city_one.daily.temperature_min[day] 
    
    cordinates_city_two = OpenMeteoGeo(city_name=second_city_name).get_city_cordinates()
    weather_for_city_two = OpenMeteoWeather(latitude=cordinates_city_two[0], longitude=cordinates_city_two[1]).get_city_weather_info()
    country_code_city_two = cordinates_city_two[2]
    avarage_temperature_city_two = weather_for_city_two.daily.temperature_min[day] + weather_for_city_two.daily.temperature_min[day]
    
    first_city_info = CityTemperature(name=city_name, country_code=country_code_city_one, avarage_temperature=avarage_temperature_city_one)
    second_city_info = CityTemperature(name=second_city_name, country_code=country_code_city_two, avarage_temperature=avarage_temperature_city_two)
    
    return WeatherStringFormat.compare_temperature(first_city_info, second_city_info)

def get_days_weather(city_name: str, days: int = 3) -> list[WeatherDay]:

    cordinates = OpenMeteoGeo(city_name=city_name).get_city_cordinates()
    city_weather = OpenMeteoWeather(latitude=cordinates[0], longitude=cordinates[1]).get_city_weather_info()
    country_code = cordinates[2]

    daily = city_weather.daily

    return [
        WeatherDay(
            time=daily.time[i],
            temperature_max=daily.temperature_max[i],
            temperature_min=daily.temperature_min[i],
            weather_code=daily.weather_code[i]
        )
        for i in range(days)
    ], country_code

def get_weather_for_multiple_days(city_name: str , days: int = 3 ):
    list_days_weather, country_code = get_days_weather(city_name, days)
    
    return WeatherStringFormat.multiple_days_weather_format(city_name, days, list_days_weather, country_code)

compare_weather("Chicago", "Kielce", day=3)

    
