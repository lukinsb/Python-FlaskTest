import requests
import urllib.parse
import json


def geocode(location):
    try:
        r = requests.get("https://api.mapbox.com/geocoding/v5/mapbox.places/" + urllib.parse.quote(location) +
                         ".json?access_token=pk.eyJ1IjoibHVjYXNiYWlhbyIsImEiOiJjanc5cWRydG4wMDNzNDhuMjB1NnYxcn"
                         "Y3In0.POE5CZ-9eWq5jxEhC30yNQ")

    except requests.exceptions.RequestException as e:
        # print(e)
        return 0, '0', 0, 0


    response = json.loads(r.text)

    if "message" in response:
        return 0, '0', 0, 0

    elif "features" in response and len(response["features"]) == 0:
        return 2, '0', 0, 0

    else:
        return 3,\
               response["features"][0]["place_name"], \
               response["features"][0]["center"][1], \
               response["features"][0]["center"][0]