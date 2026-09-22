from Questionary import *

def complete_menu():
    city_name = start_menu()

    while True:
        city_name = main_menu(city_name)

if __name__ == "__main__":
    complete_menu()