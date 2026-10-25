from nicegui import *
from Service.WeatherAPIService import *
from dataclasses import asdict
from nicegui_builder import form

ui.label("Weather APP")

with ui.card():
    city_name = ui.input("Miasto")

    def city_list_fn():
        city_list = OpenMeteoGeo(city_name.value).get_city_list()
        city_select.set_options(form(WeatherGeoForAPI, city_list))

    city_select = ui.select([], label="Wybierz Miasto")
    
    search_button = ui.button("Search", on_click=city_list_fn)






ui.run()