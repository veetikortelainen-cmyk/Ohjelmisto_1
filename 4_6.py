# Importataan random ja kysytään pisteiden määrä nelijön ja ympyrän sisällä yhteensä
# n = ympyrän sisällä olevat pisteet


import random

lkm = int(input("Kuinka monta pistettä laitetaan: "))
a = 0
n = 0

# Lasketaan pisteiden määrä ympyrässä
while a <= lkm:
    x = random.randint(-1, 1)
    y = random.randint(-1, 1)
    a += 1
    if x ** 2 + y**2 < 1:
        n += 1
# Lasketaan pii:n likiarvo

piinlikiarvo = 4*lkm/n
print(f"Pii:n likiarvo on {piinlikiarvo:.2f}")

# jos n on 0 ohjelma ei toimi en tiedä miten korjata