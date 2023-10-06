# All the exercies from week 2 #

def name():
    # Prints a result of 'hello {name}'
    return "Hello, " + input('Hello, what is your name?\n >>>' + "Good to meet you!")


def celsius2fahrenheit():
    # Prints a result of 38.4 conversion celsius to fahrenheit with the standard equation (C * (9/5)) + 32
    temp = input('What is the temprature in Celsius? \n >>> ')
    return str(temp) + ' Celsius is ' + str(temp * (9 / 5) + 32) + ' Fahrenheit'


def poppleton():
    # Prints how many groups can be made with each size of students with how many left any students
    LabSize = input('Input The Size of Lab\n >>>')
    NoStudents = input('Input The Number of Students\n >>>')
    NumberOfGroups = NoStudents // LabSize
    LeftOver = NoStudents % LabSize
    print('There will be' + str(NumberOfGroups) + ' groups with ' + str(LeftOver) + ' left over\n')


def Sweets():
    # prints the amount a teacher would have to evenly split sweets across the class
    NoStudents = input('How many students do you have?\n >>>')
    NoSweets = input('How many sweets do you have?\n >>>')
    SweetsPP = NoSweets // NoStudents
    SweetsLO = NoSweets % NoStudents
    return 'As the Teacher you would have to give each student ' + str(SweetsPP) + ' and you would have ' + str(
        SweetsLO) + ' left over'
