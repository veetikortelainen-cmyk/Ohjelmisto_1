# x on salasana ja y on käyttäjätunnus

x = "rules"
y = "Phyton"
yritys = 1

while True:
    a = input("Anna käyttäjätunnus: ")
    b = input("Anna salasana: ")
    if a == y and b == x:
        print("Tervetuloa")
        break
    elif yritys == 5:
        print("Pääsy evätty")
        break
    else:
        print("Salasana tai käyttäjätunnus oli väärin")
        yritys += 1





