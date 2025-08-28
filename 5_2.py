luvut = []

while True:
    merk = input("Anna luku: ")
    if merk == "":
        break
    else:
        luku = float(merk)
        luvut.append(luku)
luvut.sort(reverse = True)

for x in luvut:
    print(x)
