import random

print("Luodaan kaksi numerolukon koodia: ")
print("")
# Neljän numeron pituinen koodi

num1 = random.randint(0,9)
num2 = random.randint(0,9)
num3 = random.randint(0,9)
num4 = random.randint(0,9)

koodi1 = num1, num2, num3, num4
# Kolmen numeron pituinen koodi

num2_1 = random.randint(1,6)
num2_2 = random.randint(1,6)
num2_3 = random.randint(1,6)

koodi2 = num2_1, num2_2, num2_3
# Tulostetaan satunnaiset numerolukon koodit
# Ensin neljän numeron pituinen ja seuraavaksi kolmen numeron pituinen

print(f"Numerolukon koodi: {koodi1}")
print(f"Toisen numerolukon koodi: {koodi2}")