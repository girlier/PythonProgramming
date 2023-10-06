# All the Exercises from Week 4 #

#  ▄▀▀▄    ▄▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀█▄▄▄▄  ▄▀▀▄ █      ▄▀▀▀█▄    ▄▀▀▀▀▄   ▄▀▀▄ ▄▀▀▄  ▄▀▀▄▀▀▀▄
# █   █    ▐  █ ▐  ▄▀   ▐ ▐  ▄▀   ▐ █  █ ▄▀     █  ▄▀  ▀▄ █      █ █   █    █ █   █   █
# ▐  █        █   █▄▄▄▄▄    █▄▄▄▄▄  ▐  █▀▄      ▐ █▄▄▄▄   █      █ ▐  █    █  ▐  █▀▀█▀
#   █   ▄    █    █    ▌    █    ▌    █   █      █    ▐   ▀▄    ▄▀   █    █    ▄▀    █
#    ▀▄▀ ▀▄ ▄▀   ▄▀▄▄▄▄    ▄▀▄▄▄▄   ▄▀   █       █          ▀▀▀▀      ▀▄▄▄▄▀  █     █
#          ▀     █    ▐    █    ▐   █    ▐      █                             ▐     ▐
#                ▐         ▐        ▐           ▐

def NumberValid():
    number = int(input('Write a number between 0-100'))
    if 0 <= number <= 100:
        print('The Number is valid')
    else:
        print('The Number is invalid')


def Upper_Lower():
    string = input('Input a string')
    Upper = 0
    Lower = 0
    for x in string:
        if x.isupper():
            Upper += 1
        elif x.islower():
            Lower += 1
    print(f'There is {Upper} Uppercase letters and {Lower} Lowercase Letters')


def greetings():
    YourName = input('Hello, what is your name?\n >>>')
    FixedName = ''
    if YourName == '':
        YourName = 'Stranger'
    for char in enumerate(YourName):
        if FixedName = '':
            FixedName += char.upper()
        else:
            FixedName += char.lower()
    print(f'Hello, {FixedName}  Good to meet you!')


def String():
    string = input('Input a string')
    if len(string) != 1:
        print(string)
    else:
        print(string[:-1])


def celsius2fahrenheit():
    Celsius = float(input('What is the temperature in Celsius? \n >>> '))
    Fahrenheit = Celsius * 9 / 5 + 32
    print(f'{Celsius} Celsius is {Fahrenheit} Fahrenheit')


def fahrenheit2celsius():
    Fahrenheit = float(input('What is the temperature in Fahrenheit? \n >>> '))
    Celsius = (((Fahrenheit-32)*5)/9)
    print(f'{Fahrenheit} Fahrenheit is {Celsius} Celsius')
