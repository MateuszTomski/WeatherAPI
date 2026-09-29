from pydantic import BaseModel, Field, TypeAdapter
from enum import IntEnum, Enum
import random

from enum import Enum

class WeatherCode(Enum):
    clearsky = "czyste niebo"
    cloud = "pochmurnie"
    fog = "mgła"
    rain = "deszcz"
    snow = "śnieg"
    thunderstorm = "burza"
    unknown = "Nieznana"

    @classmethod
    def get_values(cls, value: int) -> str:
        
        if value == 0:
            return cls.clearsky.value

        if value in range(1, 4):
            return cls.cloud.value

        if value in (45, 48):
            return cls.fog.value

        if value in range(51, 68) or value in range(80, 83):
            return cls.rain.value

        if value in range(71, 78) or value in range(85, 87):
            return cls.snow.value

        if value in range(95, 100):
            return cls.thunderstorm.value

        return cls.unknown.value

class DayNight(Enum):
    day = "Dzien"
    night = "Noc"

    @classmethod
    def get_values(cls ,values):
        if values == 1:
            return cls.day.value
        if values == 0:
            return cls.night.value

class WeatherDailyRequest(BaseModel):
    temperature_2m_max: list[float]
    temperature_2m_min: list[float]
    weather_code: list[int]

class WeatherHourlyRequest(BaseModel):
    temperature_2m: list[float]
    rain: list[float]
    showers: list[float]
    snowfall: list[float]
    snow_depth: list[float] | None = None
    weather_code: list[int]
    wind_speed_10m: list[float]
    visibility: list[float] | None = None
    cloud_cover: list[int] | None = None

class WeatherCurrentRequest(BaseModel):
    temperature_2m: float
    rain: float
    snowfall: float
    showers: float
    weather_code: int
    wind_speed_10m: float
    is_day: int

class WeatherDailyResponse(BaseModel):
    time: list[str]
    temperature_2m_max: list[float]
    temperature_2m_min: list[float]
    weather_code: list[int]

class WeatherUnitsDailyResponse(BaseModel):
    temperature_2m_max : str
    temperature_2m_min : str


class WeatherHourlyResponse(BaseModel):
    time: list[str]
    temperature_2m: list[float]
    rain: list[float]
    showers: list[float]
    snowfall: list[float]
    snow_depth: list[float] | None = None
    weather_code: list[int]
    wind_speed_10m: list[float]
    visibility: list[float] | None = None
    cloud_cover: list[int] | None = None

class WeatherCurrentResponse(BaseModel):
    time: str
    temperature_2m: float
    rain: float
    snowfall: float
    showers: float
    weather_code: int
    wind_speed_10m: float
    is_day: int




class WeatherUnitCurrentResponse(BaseModel):
    temperature_unit : str = Field(alias="temperature_2m")
    wind_speed: str = Field(alias="wind_speed_10m")

class WeatherResponse(BaseModel):
    latitude: float
    longitude: float
    hourly: WeatherHourlyResponse
    current: WeatherCurrentResponse
    current_units: WeatherUnitCurrentResponse
    daily: WeatherDailyResponse
    daily_units: WeatherUnitsDailyResponse


class WeatherFormatParams(Enum):
    hourly = ",".join(WeatherHourlyRequest.model_fields.keys())
    current = ",".join(WeatherCurrentRequest.model_fields.keys())
    daily = ",".join(WeatherDailyRequest.model_fields.keys())
    


class WeatherGeo(BaseModel):
    name: str 
    country_code: str
    latitude: float 
    longitude: float 
    timezone: str
    country: str

class WeatherGeoList(BaseModel):
    name: str
    latitude: float 
    longitude: float 
    country: str
    country_code: str

class WeatherDay(BaseModel):
    time: str
    temperature_max: float
    temperature_min: float
    weather_code: int







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
        print(f"Pogoda na dzisiaj w {country_code} {city_name} \nData: {weather.daily.time[0]} \nMaksymalna Temperatura: {weather.daily.temperature_max[0]}{weather.daily_units.temperature_unit_max} \nNajnizsza Temperatura {weather.daily.temperature_min[0]}{weather.daily_units.temperature_unit_max} \nPogoda: {WeatherCode.get_values(weather.daily.weather_code)}")

    @staticmethod
    def current_weather_format(city_name: str , weather: WeatherDailyResponse, country_code : str) -> str:
        print(f"Obecna pogoda w {country_code} {city_name}, Czas: {weather.current.time}, Temperatura: {weather.current.temperature_2m}{weather.current_units.temperature_unit}, Deszcz {weather.current.rain}, Snieg {weather.current.snowfall}, Mzawka {weather.current.showers}, Pogoda: {WeatherCode.get_values(weather.current.weather_code)}, Pora Dnia: {DayNight.get_values(weather.current.is_day)}")

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