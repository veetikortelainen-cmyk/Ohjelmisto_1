vuosi = int(input("Anna vuosi: "))

if not (vuosi % 4 ==0 or vuosi % 100 == 0 and vuosi % 400 == 0):
    print(f"Vuosi {vuosi} ei ole karkausvuosi.")
elif (vuosi % 4 == 0 and vuosi % 100 == 0 and vuosi % 400 != 0):
    print(f"Vuosi {vuosi} ei ole karkausvuosi.")
else:
    print(f"Vuosi {vuosi} on karkausvuosi.")