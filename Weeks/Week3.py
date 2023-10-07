# All the exercises for week 3 #

# ▄ ▄   ▄███▄   ▄███▄   █  █▀        ▄▄▄▄▀ ▄  █ █▄▄▄▄ ▄███▄   ▄███▄
# █   █  █▀   ▀  █▀   ▀  █▄█       ▀▀▀ █   █   █ █  ▄▀ █▀   ▀  █▀   ▀
# █ ▄   █ ██▄▄    ██▄▄    █▀▄           █   ██▀▀█ █▀▀▌  ██▄▄    ██▄▄
# █  █  █ █▄   ▄▀ █▄   ▄▀ █  █         █    █   █ █  █  █▄   ▄▀ █▄   ▄▀
# █ █ █  ▀███▀   ▀███▀     █         ▀        █    █   ▀███▀   ▀███▀
# ▀ ▀                    ▀                  ▀    ▀

def name():
    # Prints a result of 'hello {name}'
    YourName = input('Hello, what is your name?\n >>>')

    # Checks if there is no input
    if YourName == '':
        YourName = 'Stranger'
    print(f'Hello, {YourName}  Good to meet you!')


def password():
    # Sets every password to false
    Valid = False
    BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

    # Tests all the conditions until the input passes all checks
    while not Valid:
        password1 = input('Enter Password: ')
        password2 = input('Enter your Password Again')

        # Checks if the password matches
        if password == password2:
            print('Passwords do not match')

        # Checks if the password is more than 8 and less than 12 characters long
        elif not (8 <= len(password1) <= 12):
            print('Your password must be between 8 and 12 characters long')

        # Checks if the password is in the list of bad passwords
        elif password1 in BAD_PASSWORDS:
            print('Your password is too common!')
        else:
            print('Password Set!')
            Valid = True


def times_table():
    number = int(input('Input a Number from 0-12'))

    # Checks if the number is less 8
    while True:
        if -12 <= number <= 12:
            break
        else:
            print('That is not a valid number, try again!')

    # If the number is negative it will print it backwards
    if number < 0:
        for i in range(13):
            result = (12 - number) * i
            print(f'{12 - i} x {12 - number} = {result}')

    # If it is not negative will print ascending numbers
    else:
        for i in range(13):
            result = number * i
            print(f'{i} x {number} = {result}')

