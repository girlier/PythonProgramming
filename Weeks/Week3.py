# All the exercies for week 3 #

# ▄ ▄   ▄███▄   ▄███▄   █  █▀        ▄▄▄▄▀ ▄  █ █▄▄▄▄ ▄███▄   ▄███▄
# █   █  █▀   ▀  █▀   ▀  █▄█       ▀▀▀ █   █   █ █  ▄▀ █▀   ▀  █▀   ▀
# █ ▄   █ ██▄▄    ██▄▄    █▀▄           █   ██▀▀█ █▀▀▌  ██▄▄    ██▄▄
# █  █  █ █▄   ▄▀ █▄   ▄▀ █  █         █    █   █ █  █  █▄   ▄▀ █▄   ▄▀
# █ █ █  ▀███▀   ▀███▀     █         ▀        █    █   ▀███▀   ▀███▀
# ▀ ▀                    ▀                  ▀    ▀

def name():
    # Prints a result of 'hello {name}'
    YourName = input('Hello, what is your name?\n >>>')
    if YourName == '':
        YourName = 'Stranger'
    print(f'Hello, {YourName}  Good to meet you!')


def password():
    Valid = False
    BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
    while not Valid:
        password1 = input('Enter Password: ')
        password2 = input('Enter your Password Again')
        if password == password2:
            print('Passwords do not match')
        elif not (8 <= len(password1) <= 12):
            print('Your password must be between 8 and 12 characters long')
        elif password1 in BAD_PASSWORDS:
            print('Your password is too common!')
        else:
            print('Password Set!')
            Valid = True


def Times_Table():
    table = []
    number = int(input('Input a Number from 0-12'))
    while True:
        if 8 < number <= 12:
            break
        else:
            print('That is not a valid number, try again!')
    for i in range(13):
        result = number * i
        print(f'{i} x {number} = {result}')
