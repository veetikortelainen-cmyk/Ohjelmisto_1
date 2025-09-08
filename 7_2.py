nimet = set()

nimi = input("Anna nimi: ")
nimet.add(nimi)

while nimi != "":
    nimi = input("Anna nimi voit lopettaa ohjelman tyhjällä tulostuksella: ")
    if nimi in nimet:
        print(f"Aikaisemmin annettu nimi anna uusi nimi: ")
        nimi = input("Anna uusi nimi: ")
        nimet.add(nimi)
    else:
        nimet.add(nimi)

for n in nimet:
    print(n)