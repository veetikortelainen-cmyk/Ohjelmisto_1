# Tehdään funktio jota hakiessa se summaa listan sisällä olevat arvot
# ja tulostaa saadun summan

def yht():
    summa = sum(lista)
    print(f"Antamiesi kokonaislukujen summa: {summa}")
    return

# Luodaan lista ja while loop jossa kysytään ja lisätään listaan kokonaisluvut

lista = []

a = input("Anna kokonais luku: ")

while a != "":
    if a == "":
        a = input("Anna kokonais luku: ")
    else:
        luku= int(a)
        lista.append(luku)
        a = input("Anna kokonais luku: ")
yht()

