class Hissi:
    def __init__(self, alin, ylin):
        self.sijainti = alin
        self.alin = alin
        self.ylin = ylin

    def kerros_ylös(self):
        self.sijainti += 1
        if self.sijainti > self.ylin:
            self.sijainti -= 1
            print("Hissi ei voi mennä ylemmäs")
        else:
            print(f"Olet kerroksessa: {self.sijainti}")

    def kerros_alas(self):
        self.sijainti -= 1
        if self.sijainti < self.alin:
            self.sijainti += 1
            print("Hissi ei voi mennä alemmas")
        else:
            print(f"Olet kerroksessa: {self.sijainti}")

    def siirry_kerrokseen(self, muutos):
        while self.sijainti > muutos and self.sijainti > self.alin:
            self.kerros_alas()

        while self.sijainti <muutos and self.sijainti < self.ylin:
            self.kerros_ylös()



h = Hissi(1, 5)
h.siirry_kerrokseen(5)
h.kerros_ylös()
h.kerros_alas()
h.kerros_alas()
h.siirry_kerrokseen(1)
h.siirry_kerrokseen(0)
