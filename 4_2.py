luku = float(input("Anna tuuminen määrä negatiivinen luku lopettaa ohjelman: "))
summa = 0

while luku > 0:
    summa += luku * 2.54
    print(summa)
    luku = float(input("Anna tuuminen määrä negatiivinen luku lopettaa ohjelman: "))
print(f"Loppu tuumien loppu pituus centtimetreinä {summa}cm ")
