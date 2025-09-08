airports = {}

def menu():
    while True:
        user = input(
            "Haluatko lisä uuden lentokentän tiedot (add) / etisiä lentokentän tiedot (find) / ohjelman lopettaminen komenolla (end): ")
        if user == "add":
            add_airports()
        elif user == "find":
            find_airports()
        elif user == "end":
            print("Näkemiiin ohjelma päättyy")
            break
        else:
            print("Ei virallinen komento")
            user = input(
                "Haluatko lisä uuden lentokentän tiedot (add) / etisiä lentokentän tiedot (find) / ohjelman lopettaminen komenolla (end): ")

def add_airports():
    print("")
    while True:
        finder = input("Kirjoita (continue) lisätäksesi lentokentän tai (back) palataksesi päävalikkoon: ")
        if finder == "back":
            break
        elif finder == "continue":
            name = input("Anna lentokentän nimi: ")
            icao = input("Anna lentokentän ICAO-koodi: ")
            airports[icao] = name
        else:
            print("Virheellinen komento.")

def find_airports():
    print("")
    while True:
        finder = input("Syötä lentokentän ICAO-tunnus tai palata päävalikkoon (back): ")
        if finder == "back":
            break
        else:
            print("Hakemasi lentokenttä: ", airports.get(finder))

aloita = input("Aloita ohjelma vapaalla komenolla: ")
if aloita == "end":
    print("")
    print("Näkemiin")
else:
    menu()