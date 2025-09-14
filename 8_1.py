import mysql.connector

# Vaihe 1
# muodostetaan tietokantayhteys:

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Moi12345',
         autocommit=True
         )

# Vaihe 2
# luodaan sql.kysely jolla haetaan ICOA-koodi ohjelma tulostaa koodin yhteydessä olevan lentokentän

a = input("Anna lentokentän ISOA-koodi: ")
ICOA = str.upper(a)

sql = f'select * from airport where gps_code = "{ICOA}"'

# Vaihe 3
# lähetetään kysely suoritettavaksi tietokantapalvelimelle

kursori = yhteys.cursor()
kursori.execute(sql)

tulos = kursori.fetchall()
if kursori._rowcount > 0:
    for rivi in tulos:
        print(rivi[3],"/ "+ rivi[10])
else:
    print("Ei tulostetta")