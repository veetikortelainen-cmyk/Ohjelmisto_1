suku = input("Anna biologinen sukupuolesi (mies/nainen): ")
bio = float(input("Anna hemoglobiiniarvosi (g/l)"))

if suku == "mies":
    if 134 <= bio <= 195:
        print("hemoglobiiniarvoisi ovat normaalit.")
    elif 134 >= bio:
        print("hemoglobiiniarvoisi ovat liian alhaiset.")
    else:
        print("hemoglobiiniarvoisi ovat liian suuret.")
if suku == "nainen":
    if 117 <= bio <= 175:
        print("hemoglobiiniarvoisi ovat normaalit.")
    elif 117 >= bio:
        print("hemoglobiiniarvoisi ovat liian alhaiset.")
    else:
        print("hemoglobiiniarvoisi ovat liian suuret.")