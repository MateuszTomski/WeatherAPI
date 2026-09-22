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



class WeatherDaily(BaseModel):
    time: list[str]
    temperature_max: list[float] = Field(alias="temperature_2m_max")
    temperature_min: list[float] = Field(alias="temperature_2m_min")
    weather_code: list[int]

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


