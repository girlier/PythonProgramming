# All the Exercises from Week 4 #

#  ▄▀▀▄    ▄▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀█▄▄▄▄  ▄▀▀▄ █      ▄▀▀▀█▄    ▄▀▀▀▀▄   ▄▀▀▄ ▄▀▀▄  ▄▀▀▄▀▀▀▄
# █   █    ▐  █ ▐  ▄▀   ▐ ▐  ▄▀   ▐ █  █ ▄▀     █  ▄▀  ▀▄ █      █ █   █    █ █   █   █
# ▐  █        █   █▄▄▄▄▄    █▄▄▄▄▄  ▐  █▀▄      ▐ █▄▄▄▄   █      █ ▐  █    █  ▐  █▀▀█▀
#   █   ▄    █    █    ▌    █    ▌    █   █      █    ▐   ▀▄    ▄▀   █    █    ▄▀    █
#    ▀▄▀ ▀▄ ▄▀   ▄▀▄▄▄▄    ▄▀▄▄▄▄   ▄▀   █       █          ▀▀▀▀      ▀▄▄▄▄▀  █     █
#          ▀     █    ▐    █    ▐   █    ▐      █                             ▐     ▐
#                ▐         ▐        ▐           ▐

def numbrvaild(number):
    # Checks if the number is within 0 - 100
    if 0 <= int(number) <= 100:
        return True
    else:
        return False


def upperlowerNumb(input_string) -> str:
    Upper = Lower = 0

    # Goes through each character and uses a counter system to count up every time it encounters an upper and a lower character
    for x in input_string:
        if x.isupper():
            Upper += 1
        elif x.islower():
            Lower += 1

    # Prints the amount of upper and lower characters in an input
    return f'There is {Upper} Uppercase letters and {Lower} Lowercase Letters'


def greetings(name) -> str:
    # Checks if there is no input
    if name == '':
        name = 'Stranger'

    # Prints the name with all characters capitalized except the first which is capitalised
    return f'Hello, {name.capitalize()}  Good to meet you!'


def stringMinusOne(string) -> str:
    input_string = input('Input a string')

    # Checks if the input is 1 character long
    if len(input_string) <= 1:
        return input_string

    # If the character is longer than one it slices the last character
    else:
        return input_string[:-1]


def celsius2fahrenheit(Celsius) -> str:
    Fahrenheit = (Celsius * 9 / 5 + 32)
    return str(Fahrenheit) + '°F'


def fahrenheit2celsius(Fahrenheit) -> str:
    Celsius = (((Fahrenheit-32)*5)/9)
    return str(Celsius) + '°C'

