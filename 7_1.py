vuodenaika = ("kevät",(1,2,3), "kesä", (4,5,6), "syksy", (7,8,9), "talvi", (10,11,12))

kuukausi = int(input("Anna kuukasi (1-12): "))
paikka = 1

for i in vuodenaika:
    if paikka % 2 == 0:
        if kuukausi in i:
            print("Annetun kuukaiden vuodenaika:",vuodenaika[vuodenaika.index(i)-1])
    paikka += 1