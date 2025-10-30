class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def tulosta(self):
        print(f"rekisteritunnus: {self.rekisteritunnus}")
        print(f"huippunopeus : {self.huippunopeus} km/h")
        print(f"nopeus: {self.nopeus} km/h")
        print(f"matka: {self.matka} km\n")


    def kiihdytä(self, muutos):
        self.nopeus += muutos
        if self.nopeus < 0:
            self.nopeus = 0
        elif self.nopeus >= self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kuljettu(self, matka):
        self.matka += self.nopeus * matka

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


    def tulosta_tiedot(self):
        print(f"Rekisteritunnus: {self.rekisteritunnus}")
        print(f"Huippunopeus: {self.huippunopeus}")
        print(f"Akkukapasiteetti: {self.akkukapasiteetti} kWh")
        print(f"Matka: {sähkoauto.matka:.1f} km\n")


class Polttomoottori(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatanki):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatanki = bensatanki

    def tulosta_tiedot(self):
        print(f"Rekisteritunnus: {self.rekisteritunnus}")
        print(f"Huippunopeus: {self.huippunopeus}")
        print(f"bensatanki koko: {self.bensatanki} l")
        print(f"Matka: {polttomoottori.matka:.1f} km")

sähkoauto = Sähköauto("ABC-15", 180, 52.5)
polttomoottori = Polttomoottori("ACD-123", 165, 32.3)

sähkoauto.kiihdytä(120)
polttomoottori.kiihdytä(140)
sähkoauto.kuljettu(3)
polttomoottori.kuljettu(3)
sähkoauto.tulosta_tiedot()
polttomoottori.tulosta_tiedot()
