# Tuodaan random
# Tehdään funktio jossa on random komento

import random

print("Ohjelma tulostaa nopan heittämää arvon niin kauan kuin se saa arvon 6")
def noppa():
     return random.randint(1, 6)

# Muodostetaan while silmukka jossa haetaan funktiossa oleva random ja tulostetaan saatu silmäluku
# niin kauan kuin se saa silmäluvun 6

luku = 0
while luku != 6:
    luku = noppa()
    print(f"Noppa sai simäluvuksi: {luku}")
    noppa()

