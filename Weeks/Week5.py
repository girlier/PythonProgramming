# All the Exercises from week 5

#  ▄█     █▄     ▄████████    ▄████████    ▄█   ▄█▄         ▄████████  ▄█   ▄█    █▄     ▄████████
# ███     ███   ███    ███   ███    ███   ███ ▄███▀        ███    ███ ███  ███    ███   ███    ███
# ███     ███   ███    █▀    ███    █▀    ███▐██▀          ███    █▀  ███▌ ███    ███   ███    █▀
# ███     ███  ▄███▄▄▄      ▄███▄▄▄      ▄█████▀          ▄███▄▄▄     ███▌ ███    ███  ▄███▄▄▄
# ███     ███ ▀▀███▀▀▀     ▀▀███▀▀▀     ▀▀█████▄         ▀▀███▀▀▀     ███▌ ███    ███ ▀▀███▀▀▀
# ███     ███   ███    █▄    ███    █▄    ███▐██▄          ███        ███  ███    ███   ███    █▄
#  ▀███▀███▀    ██████████   ██████████   ███   ▀█▀        ███        █▀    ▀██████▀    ██████████
#                                         ▀

# Imports
import sys
import math


# Will print the name of the Operating System that the code is run on
def version():
    os = sys.platform
    oslist = [
        ['darwin', 'MacOS'],
        ['win32', 'Windows (32-bit)'],
        ['win64', 'Windows (64-bit)'],
        ['linux', 'Linux'],
        ['linux2, Linux']
    ]
    for i in range(len(oslist)):
        if os == oslist[i][0]:
            os = oslist[i][1]
            break
    print(f'This code is running on {os}')


# Prints the number of arguments in within the command-line
def arguments():
    numberOfArgv = len(sys.argv)
    print(f'There are {numberOfArgv} arguments in the command line')


# Tests if a number input is prime or not and prints the answer
def isprime():
    n = int(input('Input a number >>>'))
    if n <= 1:
        print('Not Prime')
    elif n <= 3:
        print('Prime')
    elif n % 2 == 0 or n % 3 == 0:
        print('Not Prime')
    else:
        sqrtnumber = math.sqrt(n)
        for i in range(5, sqrtnumber + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                print('Not Prime')


# Prints an input with removed spaces and reversed
def obfuscation():
    string = input('Write a string >>>')
    print((string.replace(" ", ""))[::-1])

  def encrypt():
      string = input('Write a string >>> ')