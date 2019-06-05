from flask import Flask, request, jsonify
import argparse
from utils.geocode import geocode
from utils.weather import weather
import time

app = Flask("FlaskTest")


# parser = argparse.ArgumentParser(description='Make weather consults by the location name')
# parser.add_argument('location', metavar='Location', type=str,help='Location name for the weather search')
# args = parser.parse_args()


def weather_api():

    status, local, latitude, longitude = geocode(request.args.get("local"))
    if status == 0:
        return "Erro na requisição de localidade"
    elif status == 2:
        return "Cidade não encontrada"

    status, tempo, temperatura, chuva = weather(latitude, longitude)

    if status == 0:
        return "Erro na requisição de previsão do tempo"

    else:
        return ("Em " + local + ", está " + str.lower(tempo) + ", com temperatura de " + str(temperatura) +
                ' graus celsius e ' + str(chuva * 100) + "% de chance de chuva.")





app.add_url_rule('/weather', endpoint="weather", view_func=weather_api)

app.run(host='0.0.0.0', port=3500, debug=True, use_reloader=True, threaded=True)
