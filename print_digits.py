import pyfirmata


board = pyfirmata.Arduino('COM3')

digits = {
    0: [3, 4, 6, 8, 9, 11],
    1: [6, 8],
    2: [3, 4, 8, 9, 12],
    3: [4, 6, 8, 9, 12],
    4: [6, 8, 11, 12],
    5: [4, 6, 9, 11, 12],
    6: [3, 4, 6, 9, 11, 12],
    7: [6, 8, 9],
    8: [3, 4, 6, 8, 9, 11, 12],
    9: [4, 6, 8, 9, 11, 12]
}


def print_digits() -> None:
    """Show on sc56-11gwa entered digit."""
    try:
        digit = int(input('Enter a digit in range from 0 to 9: '))

        if -1 < digit < 10:
            for i in [3, 4, 6, 8, 9, 11, 12]:
                board.digital[i].write(0)
            for i in digits.get(digit):
                board.digital[i].write(1)
        else:
            print('Yoy enter digit not in range from 1 to 9!')

    except ValueError:
        print('You enter not a digit!')


if __name__ == '__main__':
    while True:
        print_digits()
