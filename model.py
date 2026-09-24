from pydantic import BaseModel, Field
from enum import IntEnum, Enum

class WeatherCode(Enum):
    clearsky = "czyste niebo"
    rain = "deszcz"
    snow = "snieg"
    thundersotmr = "burza"
    cloud = "pochmurnie"
    unknown = "Nieznana"

    @classmethod
    def get_values(cls, value):
        if value == 0:
            return cls.clearsky.value
        if value in range(61,65):
            return cls.rain.value
        if value in range(71,75):
            return cls.snow.value
        if value in range (95,99):
            return cls.cloud.value
        if value in range(1,3):
            return cls.cloud.value

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


class WeatherUnitsDaily(BaseModel):
    temperature_unit_max : str = Field(alias="temperature_2m_max")
    temperature_unit_min : str = Field(alias="temperature_2m_min") 


class WeatherDaily(BaseModel):
    time: list[str]
    temperature_max: list[float] = Field(alias="temperature_2m_max")
    temperature_min: list[float] = Field(alias="temperature_2m_min")
    weather_code: list[int]

class WeatherUnitCurrent(BaseModel):
    temperature_unit : str = Field(alias="temperature_2m")
    wind_speed: str = Field(alias="wind_speed_10m")


class WeatherCurrent(BaseModel):
    time: str
    temperature_2m: float
    rain: float
    snowfall: float
    showers: float
    weather_code: int
    wind_speed_10m: float
    is_day: int

class WeatherGeo(BaseModel):
    name: str 
    country_code: str
    latitude: float 
    longitude: float 
    timezone: str
    country: str

class WeatherDay(BaseModel):
    time: str
    temperature_max: float
    temperature_min: float
    weather_code: int

class Weather(BaseModel):
    latitude: float
    longitude: float
    current: WeatherCurrent
    daily: WeatherDaily
    daily_units: WeatherUnitsDaily 
    current_units: WeatherUnitCurrent

class WeatherFormat(Enum):
    daily = "daily"
    current = "current"
    hourly = "hourly"


class WeatherStringFormat():

    @staticmethod
    def daily_weather_format(city_name , weather: Weather) -> str:
            return f"Pogoda na dzisiaj w {city_name} \nData: {weather.daily.time[0]} \nMaksymalna Temperatura: {weather.daily.temperature_max[0]}{weather.daily_units.temperature_unit_max} \nNajnizsza Temperatura {weather.daily.temperature_min[0]}{weather.daily_units.temperature_unit_max} \nPogoda: {WeatherCode.get_values(weather.daily.weather_code)}"

    @staticmethod
    def current_weather_format(city_name , weather: Weather) -> str:
            return f"Obecna pogoda w {city_name}, Czas: {weather.current.time}, Temperatura: {weather.current.temperature_2m}{weather.current_units.temperature_unit}, Deszcz {weather.current.rain}, Snieg {weather.current.snowfall}, Mzawka {weather.current.showers}, Pogoda: {WeatherCode.get_values(weather.current.weather_code)}, Pora Dnia: {DayNight.get_values(weather.current.is_day)}"

