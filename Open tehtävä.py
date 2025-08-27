nimet = []
nimi = input("Anna kaverin nimi lopeta entter:illä: ")
while nimi != "":
    nimet.append(nimi)
    nimi = input("Anna kaverin nimi: ")

for nimi in nimet:
    print(f"Moi moi {nimi}")



