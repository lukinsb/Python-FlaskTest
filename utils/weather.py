import requests
import json


def weather(latitude, longitude):
    try:
        r = requests.get(
            'https://api.darksky.net/forecast/7fff670547681c9e8767ebc912b995de/' + str(latitude) + ',' + str(
                longitude) + '?lang=pt&units=si')

    except requests.exceptions.RequestException as e:
        # print(e)
        return 0, '0', 0, 0

    response = json.loads(r.text)

    if "code" in response:
        return 0, '0', 0, 0

    else:
        return 2,\
               response["currently"]["summary"],\
               response["currently"]["temperature"],\
               response["currently"]["precipProbability"]
