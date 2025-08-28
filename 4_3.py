luvut = []

while True:
    merk =input("Anna luku lopeta ohjelman tyhjällä komennolla: ")
    if merk == "":
        break
    else:
        luku = float(merk)
        luvut.append(luku)
luvut.sort()
print(f"Suurin antamasi arvo: {max(luvut)}")
print(f"Pienin antamasi arvo: {min(luvut)}")