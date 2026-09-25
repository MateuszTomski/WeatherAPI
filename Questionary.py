import questionary
from OpenMeteoService import *
import sys

def start_menu():
    city_name = questionary.text("Podaj nazwe Miasta: ").ask()
    return city_name

def main_menu(city_name):
    choice = questionary.select(
        "Co chcesz zrobić?",
        choices=[
            "Podaj obecna pogode",
            "Podaj pogode na dzisiaj",
            "Podaj pogode na jutro",
            "Podaj pogode na 3 kolejne dni",
            "Podaj inne miasto",
            "Wyjdz"
        ]
    ).ask()

    if choice == "Podaj obecna pogode":
        get_weather(city_name, wheather_format=WeatherFormat.current)

    elif choice == "Podaj pogode na dzisiaj":
        get_weather(city_name, wheather_format=WeatherFormat.daily)

    elif choice == "Podaj pogode na jutro":
        get_tommorows_weather(city_name)
    
    
    elif choice == "Podaj pogode na 3 kolejne dni":
        get_weather_for_multiple_days(city_name, days=3)



    elif choice == "Podaj inne miasto":
        return start_menu()

    elif choice == "Wyjdz":
        sys.exit()

    return city_name





