# All the exercies from week 2 #

# ▄▄▌ ▐ ▄▌▄▄▄ .▄▄▄ .▄ •▄     ▄▄▄▄▄▄▄▌ ▐ ▄▌      
# ██· █▌▐█▀▄.▀·▀▄.▀·█▌▄▌▪    •██  ██· █▌▐█▪     
# ██▪▐█▐▐▌▐▀▀▪▄▐▀▀▪▄▐▀▀▄·     ▐█.▪██▪▐█▐▐▌ ▄█▀▄ 
# ▐█▌██▐█▌▐█▄▄▌▐█▄▄▌▐█.█▌     ▐█▌·▐█▌██▐█▌▐█▌.▐▌
#  ▀▀▀▀ ▀▪ ▀▀▀  ▀▀▀ ·▀  ▀     ▀▀▀  ▀▀▀▀ ▀▪ ▀█▄▀▪

def name():
    # Prints a result of 'hello {name}'
    YourName = input('Hello, what is your name?\n >>>')
    print(f'Hello, {YourName}  Good to meet you!')


def celsius2fahrenheit():
    # Prints a result of 38.4 conversion Celsius to Fahrenheit with the standard equation (C * (9/5)) + 32
    Celsius = float(input('What is the temperature in Celsius? \n >>> '))
    Fahrenheit = Celsius * 9 / 5 + 32
    print(f'{Celsius} Celsius is {Fahrenheit} Fahrenheit')


def poppleton():
    # Gets the number of Students and size per lab #
    LabSize = float(input('Input The Size of Lab\n >>>'))
    NoStudents = float(input('Input The Number of Students\n >>>'))
    NumberOfGroups = int(NoStudents // LabSize)
    LeftOver = int(NoStudents % LabSize)

    # Prints how many groups can be made with each size of students with how many left any students
    print(f'There will be {NumberOfGroups} groups with {LeftOver} left over\n')


def Sweets():
    # Get the number of students and sweets as integers
    NoStudents = int(input('How many students do you have?\n >>>'))
    NoSweets = int(input('How many sweets do you have?\n >>>'))

    # Calculate the sweets per student and the remaining sweets
    SweetsPP = NoSweets // NoStudents
    SweetsLO = NoSweets % NoStudents

    # Prints the result as a string
    print(f'As the Teacher, you would have to give each student {SweetsPP} you would have {SweetsLO} left over')
