import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = random.randint(100, 200)
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos
        if self.nopeus < 0:
            self.nopeus = 0
        elif self.nopeus >= self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kuljettu(self, tunti):
            self.matka += self.nopeus * tunti

autot_lista = []

for auto in range(1, 11):
    autot_lista.append(Auto(f"ABC-{auto}", random.randint(100, 200)))

class kilpailu:
    def __init__(self, kilpailun_nimi, pituus_km, autot):
        self.kilpailun_nimi = kilpailun_nimi
        self.pituus_km = pituus_km
        self.autot = autot_lista

kilpailu_kaynnissa = True
tunti = 0

while kilpailu_kaynnissa:
    tunti += 1

    for auto in autot_lista:
        muutos = random.randint(-10, 15)
        auto.kiihdytä(muutos)
        auto.kuljettu(1)

        if auto.matka >= 10000:
            kilpailu_kaynnissa = False

print("KILPAILU PÄÄTTYI!\n")
print(f"Kilpailu kesti {tunti} tuntia.\n")
print(f"{'Rekisteri':<10} {'Huippu-nopeus':<8} {'Nopeus':<8} {'Matka (km)':<12}")
for auto in autot_lista:
    print(f"{auto.rekisteritunnus:<12} {auto.huippunopeus:<12} {auto.nopeus:<8}  {auto.matka:<12.0f}")

