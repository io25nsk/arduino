import pyfirmata
from time import sleep


board = pyfirmata.Arduino('COM3')

leds = {'reds': [2, 5, 8, 11],
        'yellows': [3, 6, 9, 12],
        'greens': [4, 7, 10, 13]
}

pins = list(range(2, 14))
round_pins = pins + pins[-2: 0: -1]
push_pins = list(zip(pins[:7], pins[-1:-7:-1]))
push_pins += push_pins[-2:0:-1]
jump_pins = pins[0::2] + pins[1::2]

repeat_number = 3

while True:
    for i in range(repeat_number):
        for pin in jump_pins:
            board.digital[pin].write(1)
            sleep(0.1)
        for pin in pins:
            board.digital[pin].write(0)

    for i in range(repeat_number):
        for left_pin, right_pin in push_pins:
            board.digital[left_pin].write(1)
            board.digital[right_pin].write(1)
            sleep(0.1)
            board.digital[left_pin].write(0)
            board.digital[right_pin].write(0)

    for i in range(repeat_number):
        for pin in pins:
            board.digital[pin].write(1)
            sleep(0.1)
            board.digital[pin].write(0)

    for i in range(repeat_number):
        for color in leds:
            for pin in leds[color]:
                board.digital[pin].write(1)
                sleep(0.3)
        for pin in pins:
            board.digital[pin].write(0)

    for i in range(repeat_number):
        for color in leds:
            for pin in leds[color]:
                board.digital[pin].write(1)
            sleep(0.3)
            for pin in leds[color]:
                board.digital[pin].write(0)

    for i in range(repeat_number):
        for pin in round_pins:
            board.digital[pin].write(1)
            sleep(0.1)
            board.digital[pin].write(0)
