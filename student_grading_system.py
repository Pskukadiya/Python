import statistics

admins = {'python':'pass123','python2':'pass456'}

studentDict = {'Raju':[88,56,74],
               'Shyam':[99,58,81],
               'Baburao':[78,89,63]}


def enterGrades():
    name = input('Enter Student Name: ')
    grade = input('Enter Student Grade: ')

    if name in studentDict:
        print('Grades Updating....')
        studentDict[name].append(grade)
    else:
        print('Student does not exist..')

    print(studentDict[name])


def removeStudent():
    nameToRemove = input('Enter Student Name: ')
    if nameToRemove in studentDict:
        del studentDict[nameToRemove]
        print(studentDict)
        print('Removed '+nameToRemove)
    else:
        print('Student does not exist..')

def studentAvg():
    for eachStudent in studentDict:
        gradeList = studentDict[eachStudent]
        avgGrade = statistics.mean(gradeList)

        print(eachStudent, 'has Average of ', avgGrade)


def main():
    print("""
    Welcome to Grade Central...
    [1] - Enter Grades
    [2] - Remove Students
    [3] - Student Average Grades
    [4] - Exit
    """)

    action = input("What would you like to do? (Enter a number): ")

    if action == '1':
        enterGrades()
    elif action == '2':
        removeStudent()
    elif action == '3':
        studentAvg()
    elif action == '4':
        exit()
    else:
        print('Invalid Choice')

login = input('Username : ')
passw = input('Password : ')

if login in admins:
    if admins[login] == passw:
        print('Welcome,',login)
        while True:
            main()
    else:
        print('Invalid Password')
else:
    print('Invalid Username')