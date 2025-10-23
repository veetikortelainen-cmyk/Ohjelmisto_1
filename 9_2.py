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


auto = Auto("ABC-142", 124)
auto.tulosta()
auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
auto.tulosta()
auto.kiihdytä(-200)

