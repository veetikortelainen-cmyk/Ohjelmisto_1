luku = int(input("Anna kokonaisluku: "))

if luku < 2:
   print(f"{luku} ei ole alkuluku")
elif luku == 2:
    print(f"{luku} on alkuluku")
for i in range(2, luku):
    if luku % i == 0:
        print(f"{luku} ei ole alkuluku")
        break
    else:
        print(f"{luku} on alkuluku")
        break





