from pydantic import BaseModel
from OpenMeteoModel import *

class WeatherFormat(Enum):
    daily = "daily"
    current = "current"
    hourly = "hourly"

class Accesories(Enum):
    umbrela = "umbrela"
    rainboots = "rain boots"

class Clothing(Enum):
    pass

class OutdoorActivities(Enum):
    cycling = "cycling"
    walk = "walk"
    basketball = "basketball"
    football = "football"

    @classmethod
    def suggest_random_outdoor_activity(cls):
        return random.choice(list(cls)).value

class IndoorActivities(Enum):
    laundry = "laundry"
    snow_shovel = "snow shovel"
    housechores = "house chores"
    cleaning_car = "cleaning car"

    @classmethod
    def suggest_random_activity(cls):
        return random.choice(list(cls)).value




class CityTemperature(BaseModel):
    name: str
    country_code: str
    avarage_temperature: float



class WeatherStringFormat():

    @staticmethod
    def daily_weather_format(city_name: str , weather: WeatherDailyResponse, country_code : str) -> str:
        print(f"Pogoda na dzisiaj w {country_code} {city_name} \nData: {weather.time[0]} \nMaksymalna Temperatura: {weather.temperature_max[0]}{weather.daily_units.temperature_unit_max} \nNajnizsza Temperatura {weather.daily.temperature_min[0]}{weather.daily_units.temperature_unit_max} \nPogoda: {WeatherCode.get_values(weather.daily.weather_code)}")

    @staticmethod
    def current_weather_format(city_name: str , weather: WeatherDailyResponse, country_code : str) -> str:
        print(f"Obecna pogoda w {country_code} {city_name}, Czas: {weather.time}, Temperatura: {weather.current.temperature_2m}{weather.current_units.temperature_unit}, Deszcz {weather.current.rain}, Snieg {weather.current.snowfall}, Mzawka {weather.current.showers}, Pogoda: {WeatherCode.get_values(weather.current.weather_code)}, Pora Dnia: {DayNight.get_values(weather.current.is_day)}")

    @staticmethod
    def tommorow_weather_format(city_name : str, weather: WeatherDailyResponse, country_code : str) -> str:
        print(f"Pogoda na jutro w {country_code} {city_name} \nData: {weather.daily.time[1]} \nMaksymalna Temperatura: {weather.daily.temperature_max[1]}{weather.daily_units.temperature_unit_max} \nNajnizsza Temperatura {weather.daily.temperature_min[1]}{weather.daily_units.temperature_unit_max} \nPogoda: {WeatherCode.get_values(weather.daily.weather_code)}")

    @staticmethod
    def multiple_days_weather_format(city_name: str, days, weather_days: list[WeatherDay], country_code : str):
        print(f"Pogoda w {country_code} {city_name} na {days} kolejnych dni: ")
        for weather in weather_days:
                print(f"Data: {weather.time}, Maksymalna Temperatura: {weather.temperature_max}, Minimalna Temperatura: {weather.temperature_min}, Pogoda {WeatherCode.get_values(weather.weather_code)}")
                
    @staticmethod
    def compare_temperature(temperature_city_one: CityTemperature, temperature_city_two: CityTemperature):
        
        if temperature_city_one.avarage_temperature > temperature_city_two.avarage_temperature:
            print(f"Dzisiaj w {temperature_city_one.name} {temperature_city_one.country_code} {temperature_city_one.avarage_temperature} będzie cieplej niż w {temperature_city_two.name} {temperature_city_two.country_code} {temperature_city_two.avarage_temperature} o {abs(temperature_city_one.avarage_temperature - temperature_city_two.avarage_temperature):.1f}")
        elif temperature_city_one.avarage_temperature < temperature_city_two.avarage_temperature:
            print(f"Dzisiaj w {temperature_city_one.name} {temperature_city_one.country_code} {temperature_city_one.avarage_temperature} będzie chłodniej niż w {temperature_city_two.name} {temperature_city_two.country_code} {temperature_city_two.avarage_temperature} o {abs(temperature_city_one.avarage_temperature - temperature_city_two.avarage_temperature):.1f}")
        elif temperature_city_one.avarage_temperature == temperature_city_two.avarage_temperature:
            print(f"Dzisiaj pogoda w {temperature_city_one.name} oraz {temperature_city_two.name} będzie taka sama")