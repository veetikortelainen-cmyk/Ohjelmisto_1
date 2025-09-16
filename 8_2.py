import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='Moi12345',
    autocommit=True
)

a = input("Maakoodi: ")
maakoodi = str.upper(a)

sql = f'select type, count(*) from airport where iso_country = "{maakoodi}" group by type'

kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()

if kursori.rowcount > 0:
    print(f"Lentokentät maassa {maakoodi }:")
    for tyyppi, maara in tulos:
        print(f" - {tyyppi}: {maara} kpl")
else:
    print("Ei tulostetta")