# Importataan random ja kysytään pisteiden määrä nelijön ja ympyrän sisällä yhteensä
# n = ympyrän sisällä olevat pisteet


import random

lkm = int(input("Kuinka monta pistettä laitetaan: "))
a = 0
n = 0

# Lasketaan pisteiden määrä ympyrässä
while a <= lkm:
    x = float(random.randint(-1, 1))
    y = float(random.randint(-1, 1))
    a += 1
    if x ** 2 + y**2 < 1:
        n += 1
# Lasketaan pii:n likiarvo
if n <= 0:
    print("Ympyrän sisällä ei ole pistei")
else:
    piinlikiarvo = 4*lkm/n
    print(f"Pii:n likiarvo on {piinlikiarvo:.2f}")

