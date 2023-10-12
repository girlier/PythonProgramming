# All the Exercises from Week 4 #

#  ▄▀▀▄    ▄▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀█▄▄▄▄  ▄▀▀▄ █      ▄▀▀▀█▄    ▄▀▀▀▀▄   ▄▀▀▄ ▄▀▀▄  ▄▀▀▄▀▀▀▄
# █   █    ▐  █ ▐  ▄▀   ▐ ▐  ▄▀   ▐ █  █ ▄▀     █  ▄▀  ▀▄ █      █ █   █    █ █   █   █
# ▐  █        █   █▄▄▄▄▄    █▄▄▄▄▄  ▐  █▀▄      ▐ █▄▄▄▄   █      █ ▐  █    █  ▐  █▀▀█▀
#   █   ▄    █    █    ▌    █    ▌    █   █      █    ▐   ▀▄    ▄▀   █    █    ▄▀    █
#    ▀▄▀ ▀▄ ▄▀   ▄▀▄▄▄▄    ▄▀▄▄▄▄   ▄▀   █       █          ▀▀▀▀      ▀▄▄▄▄▀  █     █
#          ▀     █    ▐    █    ▐   █    ▐      █                             ▐     ▐
#                ▐         ▐        ▐           ▐


# TYPE THE FUNCTION AS PARAMETERS INSTEAD OF INPUTS

def numbrvaild():
    number = int(input('Write a number between 0-100'))

    # Checks if the number is within 0 - 100
    if 0 <= number <= 100:
        print('The Number is valid')
    else:
        print('The Number is invalid')


def upperlower():
    input_string = input('Input a string')
    Upper = Lower = 0

    # Goes through each character and uses a counter system to count up every time it encounters an upper and a lower character
    for x in input_string:
        if x.isupper():
            Upper += 1
        elif x.islower():
            Lower += 1

    # Prints the amount of upper and lower characters in an input
    print(f'There is {Upper} Uppercase letters and {Lower} Lowercase Letters')


def greetings():
    YourName = input('Hello, what is your name?\n >>>')

    # Checks if there is no input
    if YourName == '':
        YourName = 'Stranger'

    # Prints the name with all characters capitalized except the first which is capitalised
    print(f'Hello, {YourName.capitalize()}  Good to meet you!')


def string():
    input_string = input('Input a string')

    # Checks if the input is 1 character long
    if len(input_string) <= 1:
        print(input_string)

    # If the character is longer than one it slices the last character
    else:
        print(input_string[:-1])


def celsius2fahrenheit(Celsius):
    Celsius = float(Celsius)
    Fahrenheit = Celsius * 9 / 5 + 32
    print(f'{Celsius} Celsius is {Fahrenheit} Fahrenheit')


def fahrenheit2celsius():
    Fahrenheit = float(input('What is the temperature in Fahrenheit? \n >>> '))
    Celsius = (((Fahrenheit-32)*5)/9)
    print(f'{Fahrenheit} Fahrenheit is {Celsius} Celsius')

