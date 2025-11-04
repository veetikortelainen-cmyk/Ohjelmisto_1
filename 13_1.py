from flask import Flask, Response
import json

app = Flask(__name__)

def onko_alkuluku(luku1):
    if luku1 <= 1:
        return False
    if luku1 <= 3:
        return True
    if luku1 % 2 == 0 or luku1 % 3 == 0:
        return False
    i = 5
    while i * i <= luku1:
        if luku1 % i == 0 or luku1 % (i + 2) == 0:
            return False
        i += 6
    return True


@app.route('/alkuluku/<luku>')
def tarkista_alkuluku(luku):
    try:
        luku1 = int(luku)
        tulos = onko_alkuluku(luku1)

        vastaus = {
            "Number": luku1,
            "isPrime": tulos
        }
        tilakoodi = 200

    except ValueError:
        vastaus = {
            "status": 400,
            "message": "Virheellinen syöte – ei kokonaisluku."
        }
        tilakoodi = 400

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")


@app.errorhandler(404)
def page_not_found(e):
    vastaus = {
        "status": 404,
        "message": "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)