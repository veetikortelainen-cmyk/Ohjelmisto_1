from flask import Flask, Response
import json
import mysql.connector

# --- Tietokantayhteys ---
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='Moi12345',
    autocommit=True
)

app = Flask(__name__)

def hae_lentokentta(icao):
    sql = f"select ident, name from airport where ident = '{icao}'"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    tulos = kursori.fetchone()
    return tulos

@app.route('/kenttä/<icao>')
def kentta(icao):
    try:
        tulos = hae_lentokentta(icao.upper())

        if tulos:
            vastaus = {
                "ICAO": tulos["ident"],
                "Name": tulos["name"],
            }
            status = 200
        else:
            vastaus = {
                "status": 404,
                "message": f"Lentokenttää koodilla '{icao}' ei löytynyt."
            }
            status = 404

    except Exception as e:
        vastaus = {
            "status": 500,
            "message": f"Palvelinvirhe: {str(e)}"
        }
        status = 500

    jsonvast = json.dumps(vastaus, ensure_ascii=False)
    return Response(response=jsonvast, status=status, mimetype="application/json")


@app.errorhandler(404)
def page_not_found(e):
    vastaus = {
        "status": 404,
        "message": "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus, ensure_ascii=False)
    return Response(response=jsonvast, status=404, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)