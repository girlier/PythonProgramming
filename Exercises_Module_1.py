### Wanted to work more with classes, thats why I took this approach. :)
# ▬▬ι═══════ﺤ Global Variables -═══════ι▬▬ #
Inputable = True

class ExerciseOne:

    def HelloWorld():
        # Sends a result of 'hello world'
        return 'hello world'

    def Name():
        # Returns a result of 'hello {name}'
        return "Hello " + input('What is your name?\n >>>')

    def CelsiusToFahrenheit():
        # Returns a result of 38.4 conversion celsius to fahrenheit with the standard equation (C * (9/5)) + 32
        temp = 38.4
        return str(temp) + ' Celsius is ' + str(temp * (9/5) + 32) + ' Fahrenheit'

    def Batting():
        # Returns the Batting average of Geoffery rounded to 1dp 
        Matches = 609
        Batted = 1014
        NOUT = 162
        Runs = 48426
        return "Geoffery Boycott's Batting average is: " + str(round(Runs / (Batted - NOUT))) + '% (1dp)'

    def Poppleton():
        # Returns how many groups can be made with each size of students with how many left any students
        LabSize = 24
        Numb = 0
        NoStudents = [113, 175, 12]
        groupStats = [[0, 0], [0, 0], [0,0]]
        groupCalc = [0, 0, 0]
        for n in NoStudents:
            groupStats[Numb][0] = n // LabSize
            groupStats[Numb][1] = n % LabSize
            Numb += 1
        for i in range(3):
            groupCalc[i -1] =' In group ' + str(i) + ' there would be ' + str(groupStats[i -1][0]) + ' groups with ' + str(groupStats[i-1][1]) + 'Left Overs\n'
        return groupCalc[0] + groupCalc[1] + groupCalc[2]

class ExerciseTwo:

    def Name():
        # Returns a result of 'hello {name}'
        return "Hello " + input('What is your name?\n >>>')

    def CelsiusToFahrenheit():
        # Returns a result of 38.4 conversion celsius to fahrenheit with the standard equation (C * (9/5)) + 32
        temp = input('What is the temprature in Celsius? \n >>> ')
        return str(temp) + ' Celsius is ' + str(temp * (9/5) + 32) + ' Fahrenheit'

    def Batting():
        # Returns the Batting average of Geoffery rounded to 1dp 
        Matches = input('Input The Number of matches\n >>>')
        Batted = input('Input The Number of Batted\n >>>')
        NOUT = input('Input The Number of outs\n >>>')
        Runs = input('Input The Number of Runs\n >>>')
        return "Batting average is: " + str(round(Runs / (Batted - NOUT))) + '% (1dp)'

    def Poppleton():
        # Returns how many groups can be made with each size of students with how many left any students
        LabSize = input('Input The Size of Lab\n >>>')
        NoStudents = input('Input The Number of Students\n >>>')
        NumberOfGroups = n // LabSize
        LeftOver = n % LabSize
        return groupCalc + ' There will be' + str(NumberOfGroups) + ' groups with ' + str(LeftOver) + ' left over\n'

    def Sweets():
        NoStudents = input('How many students do you have?\n >>>')
        NoSweets = input('How many sweets do you have?\n >>>')
        SweetsPP =  NoSweets // NoStudent
        SweetsLO = NoSweets % NoStudent
        return 'As the Teacher you would have to give each student ' + str(SweetsPP) + ' and you would have ' + str(SweetsLO) + ' left over'

class ExerciseThree:

    def Name():
        name = input('What is your name?\n >>>')
        if name == '':
            name = 'Stranger'
        return "Hello" + str(name)

    def CelsiusToFahrenheit():
        # Returns a result of 38.4 conversion celsius to fahrenheit with the standard equation (C * (9/5)) + 32
        temp = input('What is the temprature in Celsius? \n >>> ')
        return str(temp) + ' Celsius is ' + str(temp * (9/5) + 32) + ' Fahrenheit'

    def Batting():
        # Returns the Batting average of Geoffery rounded to 1dp 
        Matches = input('Input The Number of matches\n >>>')
        Batted = input('Input The Number of Batted\n >>>')
        NOUT = input('Input The Number of outs\n >>>')
        Runs = input('Input The Number of Runs\n >>>')
        return "Batting average is: " + str(round(Runs / (Batted - NOUT))) + '% (1dp)'

    def Poppleton():
        # Returns how many groups can be made with each size of students with how many left any students
        LabSize = input('Input The Size of Lab\n >>>')
        NoStudents = input('Input The Number of Students\n >>>')
        NumberOfGroups = n // LabSize
        LeftOver = n % LabSize
        return groupCalc + ' There will be' + str(NumberOfGroups) + ' groups with ' + str(LeftOver) + ' left over\n'

    def Sweets():
        NoStudents = input('How many students do you have?\n >>>')
        NoSweets = input('How many sweets do you have?\n >>>')
        SweetsPP =  NoSweets // NoStudent
        SweetsLO = NoSweets % NoStudent
        return 'As the Teacher you would have to give each student ' + str(SweetsPP) + ' and you would have ' + str(SweetsLO) + ' left over'

class Weeks():
    def One():
            SelectedNumber = input('What program do you want? \n 1.Hello World\n 2. Hello Name\n 3. Celsius To Faherenheit Converter\n 4. Batting Average\n 5. Poppleton grouped students calculator\n Input One of the Following: 1, 2, 3, 4, 5\n >>>')
            match SelectedNumber:
                case '1':
                    print(str(ExerciseOne.HelloWorld()) + '\n')
                case '2':
                    print(str(ExerciseOne.Name()) + '\n')
                case '3':
                    print(str(ExerciseOne.CelsiusToFahrenheit()) + '\n')
                case '4':
                    print(str(ExerciseOne.Batting()) + '\n')
                case '5':
                    print(str(ExerciseOne.Poppleton()) + '\n')
            Weeks.One()

    def Two():
            SelectedNumber = input('What program do you want? \n 1. Hello Name\n 2. Celsius To Faherenheit Converter\n 3. Batting Average\n 4. Poppleton grouped students calculator\n 5. Sharing Sweets Calc\n Input One of the Following: 1, 2, 3, 4, 5\n >>>')
            match SelectedNumber:
                case '1':
                    print(str(ExerciseTwo.Name()) + '\n')
                case '2':
                    print(str(ExerciseTwo.CelsiusToFahrenheit()) + '\n')
                case '3':
                    print(str(ExerciseTwo.Batting()) + '\n')
                case '4':
                    print(str(ExerciseTwo.Poppleton()) + '\n')
                case '5':
                    print(str(ExerciseTwo.Sweets()) + '\n')
            Weeks.Two()


def main():
    SelectedWeek = input('What Exercise do you want to pick, type a number for the week you want to select\n >>> ')
    if SelectedWeek == '1':
        Weeks.One()
    elif SelectedWeek == '2':
        Weeks.Two()

main()
                             
    
