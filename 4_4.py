import random

num = random.randint(0,10)

luku = int(input("Yritä arvoat numero väliltä 1 - 10 syötä kokonaislukuja: "))
yritys = 0
if luku == num:
    print("Arvasit oikein ensimmäisellä yrityksellä")
    yritys += 1

while luku != num:

    if luku < num:
        print("Luku jota yritätä arvat on suurempi")
        luku = int(input("Yritä uudelleen: "))
        yritys += 1
    else:
        print("Luku jota yritit arvat on pienempi")
        luku = int(input("Yritä uudelleen: "))
        yritys += 1
print("")
print(f"Sinulla meni {yritys} yritystä, että sait arvasit oikein")