# Importataan random ja kysytään pisteiden määrä nelijön ja ympyrän sisällä yhteensä
# n = ympyrän sisällä olevat pisteet


import random

lkm = int(input("Kuinka monta pistettä laitetaan: "))
a = 0
n = 0

# Lasketaan pisteiden määrä ympyrässä
while a < lkm:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    a += 1
    if x*x + y*y < 1:
        n += 1
# Lasketaan pii:n likiarvo

piinlikiarvo = 4*lkm/n
print(f"Pii:n likiarvo on {piinlikiarvo:.2f}")

