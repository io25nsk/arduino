import time
import requests
import textwrap
from pyfirmata import Arduino, util, STRING_DATA

board = Arduino('COM3')

timeout = 1

URL = 'https://fish-text.ru/get?'

payload = {'format': 'json', 'number': 5}

raw_text = requests.get(URL, params=payload).json()['text']

text = textwrap.fill(raw_text, width=16)

for word in text.split('\n'):
    board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(word))
    time.sleep(timeout)
