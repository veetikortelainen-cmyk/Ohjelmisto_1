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



auto = Auto("ABC-142", 124)
auto.tulosta()
auto.kiihdytä(60)
auto.kuljettu(1.5)
auto.tulosta()
