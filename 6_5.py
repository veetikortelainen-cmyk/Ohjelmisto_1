def yht():
    print(f"Antamiesi numeroiden lista: {lista}")
    print(f"Antamiesi numeroiden lista: {dif_by_twolist}")
    return

lista = []
dif_by_twolist = []

a = input("Anna kokonais luku: ")

while a != "":
        luku= int(a)
        if luku % 2 == 0:
            dif_by_twolist.append(luku)
            lista.append(luku)
            a = input("Anna kokonais luku: ")
        else:
            lista.append(luku)
            a = input("Anna kokonais luku: ")
yht()

