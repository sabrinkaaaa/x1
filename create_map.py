import requests
api_server = "http://static-maps.yandex.ru/1.x/"

lon = "37.530887"
lat = "55.703118"
delta = "3"

params = {
    "ll": ",".join([lon, lat]),
    "spn": ",".join([delta, delta]),
    "l": "map"
}
response = requests.get(api_server, params=params)
file = open("1.png", 'wb')
for i in response:
    file.write(i)
