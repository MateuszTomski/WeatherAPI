from OpenMeteoRepository import *
from model.WeatherAPIModel import *
import pendulum


def WeatherAPIHourly_Service(city_name: str, hours: int = 24) -> HourlyWeatherAPI:
    get_city_cordinates = OpenMeteoGeo(city_name=city_name).get_city_cordinates()
    get_hourly_weather = OpenMeteoWeather(latitude=get_city_cordinates[0], longitude=get_city_cordinates[1]).get_hourly_weather()
    return [
        HourlyWeatherAPI(
        time=get_hourly_weather.time[i],
        temperature=get_hourly_weather.temperature_2m[i],
        wind_speed=get_hourly_weather.wind_speed_10m[i],
        rain=get_hourly_weather.rain[i],
        showers=get_hourly_weather.showers[i],
        snowfall=get_hourly_weather.snowfall[i],
        snow_depth=get_hourly_weather.snow_depth[i],
        cloud_cover=get_hourly_weather.cloud_cover[i],
        visibility=get_hourly_weather.visibility[i],
        weather_code=get_hourly_weather.weather_code[i]
   )
   for i in range(hours)]

def WeatherAPIDaily_Service(city_name: str, days: int = 7) -> DailyWeatherAPI:
    get_city_cordinates = OpenMeteoGeo(city_name=city_name).get_city_cordinates()
    get_daily_weather = OpenMeteoWeather(latitude=get_city_cordinates[0], longitude=get_city_cordinates[1], forecast_days=days).get_daily_weather()
    
    return [
        DailyWeatherAPI(
        time=get_daily_weather.time[i],
        temperature_max=get_daily_weather.temperature_2m_max[i],
        temperature_min=get_daily_weather.temperature_2m_min[i],
        avarage_tempearture=(get_daily_weather.temperature_2m_max[i] + get_daily_weather.temperature_2m_min[i]) / 2,
        weather_code=get_daily_weather.weather_code[i]
    )
    for i in range(days)]

def WeatherAPICurrent_Service(city_name: str) -> CurrentWeatherAPI:
    get_city_cordinates = OpenMeteoGeo(city_name=city_name).get_city_cordinates()
    get_current_weather = OpenMeteoWeather(latitude=get_city_cordinates[0], longitude=get_city_cordinates[1]).get_current_weather()

    return CurrentWeatherAPI(
        time=get_current_weather.time,
        temperature=get_current_weather.temperature_2m,
        rain=get_current_weather.rain,
        snowfall=get_current_weather.snowfall,
        showers=get_current_weather.showers,
        weather_code=get_current_weather.weather_code,
        wind_speed=get_current_weather.wind_speed_10m,
        is_day=get_current_weather.is_day

    )


def WeatherAPI_SpecificCityInfo(city_name: str, city_id: int) -> WeatherGeoForAPI:
    get_city_info = OpenMeteoGeo(city_name=city_name).get_city_list()
    for city in get_city_info:
        if city.id == city_id:
            return city

def WeatherAPI_CityInfo(city_name: str, city_id: int) -> CityInfoAPI:
    city_info = WeatherAPI_SpecificCityInfo(city_name, city_id)

    return CityInfoAPI(
        id=city_info.id,
        name=city_info.name,
        country=city_info.country,
        country_code=city_info.country_code,
        country_id=city_info.country_id,
        timezone=city_info.timezone,
        post_code=city_info.post_code,
        latitude=city_info.latitude,
        longitude=city_info.longitude
    )

def WeatherAPI_CurrentDayWeatherAPIDay(city_name: str, city_id: int, days = 7, hours = 24) -> WeatherDayAPI:
    city = WeatherAPI_SpecificCityInfo(city_name , city_id)
    city_info = WeatherAPI_CityInfo(city.name, city.id)
    hourly = WeatherAPIHourly_Service(city.name, hours)
    daily = WeatherAPIDaily_Service(city.name, days)
    current = WeatherAPICurrent_Service(city.name)
    date_pendulum = pendulum.now()
    
    return WeatherDayAPI(
        name=city.name,
        date=str(date_pendulum.date()),
        city_info=city_info,
        current_weather=current,
        hourly_weather=hourly[:24],
        daily_weather=daily[0]
    )

def WeatherAPI_TommorowDayWeatherAPIDay(city_name: str, city_id: int, days = 7, hours = 48) -> WeatherDayAPI:
    city = WeatherAPI_SpecificCityInfo(city_name , city_id)
    city_info = WeatherAPI_CityInfo(city.name, city.id)
    hourly = WeatherAPIHourly_Service(city.name, hours)
    daily = WeatherAPIDaily_Service(city.name, days)
    date_pendulum = pendulum.tomorrow()
    
    return WeatherDayAPI(
        name=city.name,
        date=str(date_pendulum.date()),
        city_info=city_info,
        hourly_weather=hourly[24:48],
        daily_weather=daily[1]
    )




# x = WeatherAPI_CurrentDayWeatherAPIDay("Kielce", city_id=769250)
# print(x)

# for y in x:
#     print(y[1])

# x = (WeatherAPIHourly_Service("Bielawa", 72))
# print(x[24:72])

# x = WeatherAPIDaily_Service("Kielce", days=3)
# print(x)

# x = WeatherAPICurrent_Service("Kielce")
# print(x)