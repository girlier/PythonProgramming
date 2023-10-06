# All the commands from the week one exercies

# A function that prints 'Hello World' #
def helloworld():
    print('hello world')


# A function that print 'Hello Rosie'
def name():
    print('hello, rosie!')


# A function that prints the Conversion of 38.4C into Fahrenheit #
def celsius2fahrenheit():
    print(str(38.4) + ' Celsius is ' + str(38.4 * (9 / 5) + 32) + ' Fahrenheit')


# A function that returns Geoffrey Boycott's batting average #
def batting():
    print("Geoffrey Boycott's Batting average is: " + str(round(48426 / (1014 - 162))) + '% (1dp)')


# A function that displays how many groups there can be with an amount of students #
def poppleton():
    LabSize = 24
    Numb = 0
    NoStudents = [113, 175, 12]
    groupStats = [[0, 0], [0, 0], [0, 0]]
    groupCalc = [0, 0, 0]
    for n in NoStudents:
        groupStats[Numb][0] = n // LabSize
        groupStats[Numb][1] = n % LabSize
        Numb += 1
    for i in range(3):
        groupCalc[i - 1] = ' In group ' + str(i) + ' there would be ' + str(groupStats[i - 1][0]) + ' groups with ' + str(groupStats[i - 1][1]) + 'Left Overs\n'
    return groupCalc[0] + groupCalc[1] + groupCalc[2]
