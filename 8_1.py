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


a = input("Anna lentokentän ISAO-koodi: ")
ICAO = str.upper(a)

sql = f'select * from airport where ident = "{ICAO}"'


kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()

for rivi in tulos:
        print(rivi[3],"/ "+ rivi[10])
