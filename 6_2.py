import random

def noppa():
     return random.randint(1, a)

a = int(input("Kuinka monta tahkoa nopalla on: "))
while a < 2:
    if a < 2:
        a = int(input("Noppalla pitää olla vähintään kaksi tahkoa: "))
    else:
        break
luku = 0
while luku != a:
    luku = noppa()
    print(f"Noppa sai simäluvuksi: {luku}")
    noppa()

