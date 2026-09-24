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
            "Podaj pogode na 5 kolejnych dni",
            "Podaj inne miasto",
            "Wyjdz"
        ]
    ).ask()

    if choice == "Podaj obecna pogode":
        print(get_weather(city_name, wheather_format=WeatherFormat.current))

    elif choice == "Podaj pogode na dzisiaj":
        print(get_weather(city_name, wheather_format=WeatherFormat.daily))

    elif choice == "Podaj pogode na 5 kolejnych dni":
        days = days_format(city_name)
        for weather in days:
            print(weather)


    elif choice == "Podaj inne miasto":
        return start_menu()

    elif choice == "Wyjdz":
        sys.exit()

    return city_name





