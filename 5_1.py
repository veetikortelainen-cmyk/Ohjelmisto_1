import random

arp = int(input("Anna arpakuutioiden määrä: "))
summa = 0

for x in range(arp):
    num = random.randint(1, 6)
    summa += num
#   sievempi muoto:
#   summa += random.randint(1, 6)
print(f"Arpakuutioiden summa on {summa}.")