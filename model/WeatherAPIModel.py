from pydantic import BaseModel

class HourlyWeatherAPI(BaseModel):
    time: str
    max_temperature: float
    min_temperature: float
    avarage_temperature: float
    wind_speed: float
    rain: float
    showers: float
    snowfall: float
    snow_depth: float
    cloud_cover: float
    weather_code: int


class DailyWeatherAPI(BaseModel):
    time: str
    temperature_2m_max: float
    temperature_2m_min: float
    avarage_tempearture: float
    weather_code: int

class CurrentWeatherAPI(BaseModel):
    time: str
    temperature: float
    rain: float
    snowfall: float
    showers: float
    weather_code: int
    wind_speed: float
    is_day: int

class CityInfoAPI(BaseModel):
    id: int
    country: str
    country_code: str
    country_id: int
    timezone: str
    post_code: str | None = None
    latitude: float
    longitude: float


class WeatherDayAPI(BaseModel):
    name: str
    date: str
    city_info: CityInfoAPI
    current_weather: CurrentWeatherAPI
    hourly_weather: list[HourlyWeatherAPI]
    daily_weather: DailyWeatherAPI