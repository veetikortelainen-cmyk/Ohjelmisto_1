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
        print(f"matka: {self.matka} km")

auto = Auto("ABC-142", 124)
auto.tulosta()


