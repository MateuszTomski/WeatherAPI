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

class WeatherDailyResponse(BaseModel):
    time: list[str]
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

class WeatherCurrentRequest(BaseModel):
    temperature_2m: float
    rain: float
    snowfall: float
    showers: float
    weather_code: int
    wind_speed_10m: float
    is_day: int

class WeatherCurrentResponse(BaseModel):
    time: str
    temperature_2m: float
    rain: float
    snowfall: float
    showers: float
    weather_code: int
    wind_speed_10m: float
    is_day: int

class WeatherUnitsDailyResponse(BaseModel):
    temperature_2m_max : str
    temperature_2m_min : str

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

class WeatherRequestParams(Enum):
    hourly = WeatherHourlyRequest.model_fields.keys()
    current = WeatherCurrentRequest.model_fields.keys()
    daily = WeatherDailyRequest.model_fields.keys()
    
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

class WeatherGeoForAPI(BaseModel):
    id: int
    name: str
    country: str
    country_code: str
    country_id: int
    timezone: str
    post_code: str | None = None
    latitude: float
    longitude: float


class WeatherDay(BaseModel):
    time: str
    temperature_max: float
    temperature_min: float
    weather_code: int

    def convert(self, weather_response: WeatherDailyResponse, day: int):
        self.time=weather_response.time[day]
        self.temperature_max=weather_response.temperature_2m_max[day]
        self.temperature_min=weather_response.temperature_2m_min[day]
        self.weather_code=weather_response.weather_code[day]






