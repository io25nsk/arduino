import requests
from pyfirmata import Arduino, util, STRING_DATA
from time import sleep

board = Arduino('COM3')

URL = 'https://api.open-meteo.com/v1/forecast?'

latitude = 55.11
longitude = 82.93

update_period = 900

payload = {'latitude': latitude,
           'longitude': longitude,
           'current': ['temperature_2m',
                       'wind_speed_10m',
                       'wind_direction_10m']}


wind_directions = ['Nord', 'N-East', 'East', 'S-East', 'South', 'S-West', 'West', 'N-West', 'Nord']

while True:

    result = ['Current weather', f'in {latitude} {longitude}']

    weather = requests.get(URL, params=payload).json()

    temperature = str(weather['current']['temperature_2m'])
    wind_speed = weather['current']['wind_speed_10m']
    wind_azimuth = weather['current']['wind_direction_10m']
    wind_direction = wind_directions[int(wind_azimuth / 45 + 0.5)]

    result += ([f'Temp: {temperature} C'] +
               [f'Wind: {wind_speed} {wind_direction}'])

    for s in result:
        board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(s))
        sleep(3)

    sleep(update_period)
