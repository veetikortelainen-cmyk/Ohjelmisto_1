luvut = []

while True:
    merk = input("Anna luku: ")
    if merk == "":
        break
    else:
        luku = float(merk)
        luvut.append(luku)

if len(luvut)>= 5:
    luvut.sort(reverse=True)
    for x in luvut[:5]:
        print(x)
else:
    luvut.sort(reverse=True)
    for x in luvut[:5]:
        print(x)
