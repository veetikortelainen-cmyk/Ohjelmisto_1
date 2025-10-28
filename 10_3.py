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

class Talo:
    def __init__(self, alin, ylin, hissien_lkm):
        self.hissit = []
        for i in range(hissien_lkm):
            hissi = Hissi(alin, ylin)
            self.hissit.append(hissi)
            self.alin = alin

    def aja_hissiä(self, hissin_numero, muutos):
        if 0 <= hissin_numero < len(self.hissit):
            print(f"\nAjetaan hissiä {hissin_numero + 1}:")
            self.hissit[hissin_numero].siirry_kerrokseen(muutos)
        else:
            print("Virheellinen hissin numero.")

    def palohälytys(self):
        print("\nPalohälytys! Kaikki hissit palaavat pohjakerrokseen!")
        for i in range(len(self.hissit)):
            hissi = self.hissit[i]
            print(f"\nHissi {i + 1} menee pohjakerrokseen:")
            hissi.siirry_kerrokseen(self.alin)

talo = Talo(0, 10, 2)

talo.aja_hissiä(0, 7)
talo.aja_hissiä(1, 10)
talo.palohälytys()









