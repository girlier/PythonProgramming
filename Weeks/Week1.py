# All the commands from the week one exercises #



 █     █░▓█████ ▓█████  ██ ▄█▀    ▒█████   ███▄    █ ▓█████ 
▓█░ █ ░█░▓█   ▀ ▓█   ▀  ██▄█▒    ▒██▒  ██▒ ██ ▀█   █ ▓█   ▀ 
▒█░ █ ░█ ▒███   ▒███   ▓███▄░    ▒██░  ██▒▓██  ▀█ ██▒▒███   
░█░ █ ░█ ▒▓█  ▄ ▒▓█  ▄ ▓██ █▄    ▒██   ██░▓██▒  ▐▌██▒▒▓█  ▄ 
░░██▒██▓ ░▒████▒░▒████▒▒██▒ █▄   ░ ████▓▒░▒██░   ▓██░░▒████▒
░ ▓░▒ ▒  ░░ ▒░ ░░░ ▒░ ░▒ ▒▒ ▓▒   ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░░ ▒░ ░
  ▒ ░ ░   ░ ░  ░ ░ ░  ░░ ░▒ ▒░     ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ░  ░
  ░   ░     ░      ░   ░ ░░ ░    ░ ░ ░ ▒     ░   ░ ░    ░   
    ░       ░  ░   ░  ░░  ░          ░ ░           ░    ░  ░
                                                            

# A function that prints 'Hello World' #
def helloworld():
    print('hello world')


# A function that print 'Hello Rosie'
def name():
    print('hello, rosie!')


# A function that prints the Conversion of 38.4C into Fahrenheit #
def celsius2fahrenheit():
    FahrenheitTemp = 38.4 * 9 / 5 + 32
    print(f'38.4 Celsius is {FahrenheitTemp} Fahrenheit')


# A function that returns Geoffrey Boycott's batting average #
def batting():
    print(f"Geoffrey Boycott's Batting average is: {48426 / (1014 - 162)}")


# A function that displays how many groups there can be with an amount of students #
def poppleton():
    LabSize = 24
    NoStudents = [113, 175, 12]
    GroupStats = []
    GroupCalc = []

    # Does all the Calculations and puts them in the GroupStats Array #
    for n in NoStudents:
        Group = n // LabSize
        LeftOver = n % LabSize
        GroupStats.append((Group, LeftOver))

    # Combines all the GroupStats in to readable text
    for i in range(3):
        GroupCalc.append(f'In group {i+1} there would be {GroupStats[i - 1][0]} groups with {GroupStats[i - 1][1]} Left Overs\n')

    # prints the whole list
    print(''.join(GroupCalc))
