import random

arp = int(input("Anna arpakuutioiden määrä: "))
summa = 0

for x in range(arp):
    num = random.randint(1, 6)
    summa += num

print(f"Summa on {summa}")