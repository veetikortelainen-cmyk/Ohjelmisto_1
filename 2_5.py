# Pyydetään antamaan vanhanajan painon termeinä painoja

leiviska = float(input("Anna leiviskät: "))
naula = float(input("Anna naulat: "))
luoti= float(input("Anna luosit: "))

# Lasketaan joakisen vanhanan ajan termin massat ja muunnetaan g:mma kg:mmoiksi

luotimass = luoti * 0.0133
naulamass = naula * 32 * 0.0133
leivistamss = leiviska * 20 * 32 * 0.0133

# Lisätään jokaisen yksikön massat yhteen

yht = luotimass + naulamass + leivistamss

# Tulostetaan vastaus

print("Massat nykymittojen mukaan: ")
print(f"{int(yht)} kilogrammaa ja {(yht - int(yht))*1000:.2f} grammaa.")