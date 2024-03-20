import sys
import math
import csv
import copy
import re

from nodes import Student

NUMDAYS = 7

def main(form, schedule, shadows, name, order):
    # change to 4 when we input students
    '''if len(sys.argv) != 5:
        sys.exit(

            "Usage: python CaxyKeys.py form.csv schedule.csv shadows index order"
        )
    students = loadPeople(sys.argv[1], sys.argv[2])
    prospective, time = loadProspective(sys.argv[3], int(sys.argv[4]))
    students = limitStudents(students, prospective, time)
    #print(len(students))
    students = orderStudents(students, prospective, time, bool(sys.argv[5]))'''

    students = loadPeople(form, schedule)
    prospective, time = loadProspective(shadows, name)
    #print(len(students))
    students = limitStudents(students, prospective, time)
    #print(len(students))
    students = orderStudents(students, prospective, time, bool(order))

    return output(students, prospective, time)
        #print(students[i].getArts())

def sortByEmail(person):
    return person.getEmail()

# This function loads each student object based on the provided data
# Only data about the schedules is transformed, everything else is kept as strings
# for simplicity, and because inputs won't be insanely large
def loadPeople(form, schedule):
    studentList = list()
    emailList = list()
    '''with open(form) as sheet:
        reader = csv.reader(sheet)
        next(reader)'''
    #print(form)
    for num, rowx in enumerate(form.splitlines()[1:]):
        rowy = rowx.replace(', ', '^ ')
        rowy = rowy.replace('"', '')
        row = rowy.split(',')
        #print(row)
        email = row[1].lower()
        emailList.append(email)
        firstName = row[2]
        lastName = row[3]
        grade = int(row[4][:-8])
        gender = row[5]
        middleSchool = row[7]
        dayBoard = row[8]
        town = row[9]
        languages = row[10].split('^ ')
        sportsLFA = row[11].split('^ ')
        sportsNotLFA = row[12].split('^ ')
        arts = row[13].split('^ ')
        affinity = row[14].split('^ ')
        clubsMajor = row[15].split('^ ')
        clubsMinor = row[16].split('^ ')
        interests = row[17].split('^ ')
        if len(row) > 19:
            numVisits = int(row[19])
        else:
            numVisits = 0

        person =  Student(email, firstName, lastName,
        grade, gender, middleSchool, dayBoard, town, languages,
        sportsLFA, sportsNotLFA, arts, affinity, clubsMajor,
        clubsMinor, interests, numVisits)
        studentList.append(person)
    studentList = sorted(studentList, key = sortByEmail)
    emailList = [person.getEmail() for person in studentList]

    '''with open(schedule) as sheet:
        reader = csv.reader(sheet)
        next(reader)'''
    for num, rowx in enumerate(schedule.splitlines()[1:]):
        rowy = rowx.replace(', ', '^ ')
        rowy = rowy.replace('"', '')
        row = rowy.split(',')
        #print(row)
        if row[2] in emailList:
            subject = row[3]
            if subject[0:2] == "10" or subject[0:2] == "99":
                continue
            name = row[4][9:]
            period = row[8][1]
            if(not period.isdigit()):
                continue
            code = ""
            for i in range (NUMDAYS):
                if (len(row[10 + 3*i]) <= 2):
                    code += "0"
                else:
                    eleven = re.split(':| ', row[11+3*i])
                    ten = re.split(':| ',row[10+3*i])
                    if (int(eleven[0]) < 8):
                        eleven[0] = int(eleven[0]) + 12
                    if (int(ten[0]) < 8):
                        ten[0] = int(ten[0]) + 12
                    if (
                        60*int(eleven[0]) + int(eleven[1]) -
                        60*int(ten[0]) - int(ten[1]) > 45
                    ):
                        code += "2"
                    else:
                        code += "1"
            studentList[emailList.index(row[2])].setClass(
                name, subject, code, period
            )
    return studentList

def loadProspective(form, name):
    '''lines = len(open(form, 'r').readlines())
    with open(form) as sheet:
        reader = csv.reader(sheet)
        if index >= 1:
            for i in range(index):
                next(reader)
        else:
            for i in range(lines+index):
                next(reader)'''
    #print(form)
    index = -1
    for num, rowx in enumerate(form.splitlines()[1:]):
        row = rowx.split(',')
        fullName = row[2] + " " + row[3]
        if name.lower() == fullName.lower():
            index = num + 1
            break
    rowx = form.splitlines()[index]
    #print(rowx)
    rowy = rowx.replace(', ', '^ ')
    rowy = rowy.replace('"', '')
    row = rowy.split(',')
    #print(row)
    firstName = row[2]
    lastName = row[3]
    grade = int(row[4][:-8])
    gender = row[5]
    middleSchool = row[6]
    dayBoard = row[7]
    town = row[8]
    languages = row[9].split('^ ')
    sportsLFA = row[10].split('^ ')
    arts = row[11].split('^ ')
    affinity = row[12].split('^ ')
    clubs = row[13].split('^ ')
    interests = row[14].split('^ ')
    date = row[15]
    letter = row[16]
    firstPeriod = row[17]
    lastPeriod = row[18]

    person =  Student(None, firstName, lastName,
        grade, gender, middleSchool, dayBoard, town, languages,
        sportsLFA, None, arts, affinity, clubs,
        None, interests, None)
    day = [date, letter, firstPeriod, lastPeriod]
    return person, day

def limitStudents(students, prospective, date):
    savedList = copy.deepcopy(students)
    updatedList = list()

    #check gender matches
    if prospective.getGender() == 'Male':
        for student in savedList:
            if student.getGender() != 'Female':
                updatedList.append(student)
    elif prospective.getGender() == 'Female':
        for student in savedList:
            if student.getGender() != 'Male':
                updatedList.append(student)
    savedList = copy.deepcopy(updatedList)
    updatedList = list()
    
    #check grade matches ± 1
    for student in savedList:
        if student.getGrade() == prospective.getGrade() or\
            student.getGrade() == prospective.getGrade() + 1:
            updatedList.append(student)
    savedList = copy.deepcopy(updatedList)
    updatedList = list()
    
    #check boarding matches
    if prospective.getDayBoard() == 'Boarding':
        for student in savedList:
            if student.getDayBoard() == 'Boarding':
                updatedList.append(student)
        savedList = copy.deepcopy(updatedList)
        updatedList = list()
    
    #check ≥2 core classes + lunch + ≤1 frees
    #cores are 1 eng, 2 math, 3 sci, 4 hist
    #lunch is 98
    for student in savedList:
        lunchCheck = False
        numCores = 0
        numFrees = 0
        schedule = student.getDaySchedule(date[1], int(date[2]), int(date[3]))
        for course in schedule:
            #print(course)
            if course == []:
                numFrees += 1
                continue
            if int(course[1][0:2]) == 11 or\
                int(course[1][0]) == 2 or\
                int(course[1][0]) == 3 or int(course[1][0]) == 4:
                numCores += 1
            if int(course[1][0:2]) == 98:
                lunchCheck = True
        if lunchCheck == True and numCores >= 2 and numFrees <= 1:
            updatedList.append(student)
    savedList = copy.deepcopy(updatedList)
    updatedList = list()
    #print(len(savedList))

    for student in savedList:
        if student.getNumVisits() < 2:
            updatedList.append(student)
    savedList = copy.deepcopy(updatedList)
    updatedList = list()

    return savedList


#order up!
def orderStudents(students, prospective, date, order):

    checkFor = list()
    if "Mathematics" in prospective.getInterests():
        checkFor.append("21")
    if "Computer Science" in prospective.getInterests():
        checkFor.append("23")
    if "English" in prospective.getInterests():
        checkFor.append("11")

    #Some are easier to check by word
    wordCheck = list()
    if "Physics" in prospective.getInterests():
        wordCheck.append("Physics")
    if "Chemistry" in prospective.getInterests():
        wordCheck.append("Chemistry")
    if "Biology" in prospective.getInterests():
        wordCheck.append("Biology")
    if "Spanish" in prospective.getInterests():
        wordCheck.append("Spanish")
    if "French" in prospective.getInterests():
        wordCheck.append("French")
    if "Chinese" in prospective.getInterests():
        wordCheck.append("Chinese")
    if "History" in prospective.getInterests():
        wordCheck.append("History")

    artsCheck = list()
    if "2D Visual Arts" in prospective.getArts():
        artsCheck.append("Studio")
    if "Photography" in prospective.getArts():
        artsCheck.append("Photo")
    if "Ceramics" in prospective.getArts():
        artsCheck.append("Ceramics")
    if "Glass" in prospective.getArts():
        artsCheck.append("Glass")
    if "Acting" in prospective.getArts():
        artsCheck.append("Acting")
    if "Theater Tech" in prospective.getArts():
        artsCheck.append("Theater Tech")
    if "Choir/VOX/Singing" in prospective.getArts():
        artsCheck.append("Choir")
    if "Orchestra" in prospective.getArts():
        artsCheck.append("Orchestra")

    def checks(student):
        checkForCopy = copy.deepcopy(checkFor)
        wordCheckCopy = copy.deepcopy(wordCheck)
        artsCheckCopy = copy.deepcopy(artsCheck)
        count = 0
        electiveCount = 0
        words = False
        arts = False
        schedule = student.getDaySchedule(date[1], int(date[2]), int(date[3]))
        for course in schedule:
            if course == []:
                continue
            if course[1][0:2] in checkForCopy and course[1][0:3] != "119":
                count += 1
                checkForCopy.remove(course[1][0:2])
            for word in wordCheckCopy:
                if word in course[0]:
                    words = True
                    count += 1
                    wordCheckCopy.remove(word)
            for art in artsCheckCopy:
                if art in course[0]:
                    arts = True
                    count +=1
                    artsCheckCopy.remove(art)
            if (not words and course[1][0] == "5") or\
                (not arts and course[1][0] == "6") or\
                course[1][0:3] == "119":
                electiveCount += 1
        #print(count)
        #print(student.getFirstName())
        if electiveCount > 1:
            #print(student.getFirstName() + str(count - 1))
            return count - 1
        else:
            #print(student.getFirstName() + str(count))
            return count

    def sports(student):
        count = 0
        for sport in prospective.getSportsLFA():
            if sport in student.getSportsLFA():
                count += 1
        return count

    def interests(student):
        count = 0
        for aff in prospective.getAffinity():
            if aff in student.getAffinity():
                count += 1
        for club in prospective.getClubsMajor():
            if club in student.getClubsMajor():
                count += 1
        for i in prospective.getInterests():
            if i in student.getInterests():
                count += 1
        for a in prospective.getArts():
            if a in student.getArts():
                count += 1
        return count

    def languages(student):
        count = 0
        for lang in prospective.getLanguages():
            if lang in student.getLanguages():
                count += 1
        return count

    #add feature to re-sort by certain preferences
    if not order:
        students = sorted(students, reverse=True, key = lambda x: (checks(x), languages(x), sports(x), interests(x)))
    else:
        students = sorted(students, reverse=True, key = lambda x: (sports(x), checks(x), languages(x), interests(x)))
    return students


def output(students, prospective, time):
    toReturn = "Prospective student: " + prospective.getFirstName() +\
            " will visit on " + time[0] + " which is a " +\
            time[1] + " day from periods " + time[2] +\
            " to " + time[3]
    for num, stu in enumerate(students):
        toReturn += "\n"
        if num >= 5: break
        toReturn += "\n" + str(num + 1) + ". " + stu.getFirstName() + " " +\
                stu.getLastName() + ". \n Reasons:"
        if stu.getGrade() == prospective.getGrade():
            toReturn += "\n" + "Both are in grade " + str(stu.getGrade())
        if stu.getGender() == prospective.getGender():
            toReturn += "\n" + "Both are " + stu.getGender()
        if stu.getDayBoard() == prospective.getDayBoard():
            toReturn += "\n" + "Both are " + stu.getDayBoard() + " students"
        if stu.getLanguages() != ['']:
            for lang in stu.getLanguages():
                if lang in prospective.getLanguages():
                    toReturn += "\n" + "Both are fluent in " + lang
        if stu.getSportsLFA() != ['']:
            for sport in stu.getSportsLFA():
                if sport in prospective.getSportsLFA():
                    toReturn += "\n" + "Both play " + sport
        if stu.getArts() != ['']:
            for art in stu.getArts():
                if art in prospective.getArts():
                    toReturn += "\n" + "Both enjoy " + art
        if prospective.getAffinity() != ['']:
            for aff in stu.getAffinity():
                if aff in prospective.getAffinity():
                    toReturn += "\n" + "Both are interested in " + aff
        if prospective.getClubsMajor() != ['']:
            for club in stu.getClubsMajor():
                if club in prospective.getClubsMajor():
                    toReturn += "\n" + "Both are interested in " + club
        if prospective.getInterests() != ['']:
            for interest in stu.getInterests():
                if interest in prospective.getInterests():
                    toReturn += "\n" + "Both are interested in " + interest

        checkFor = list()
        if "Mathematics" in prospective.getInterests():
            checkFor.append("21")
        if "Computer Science" in prospective.getInterests():
            checkFor.append("23")
        if "English" in prospective.getInterests():
            checkFor.append("11")

        #Some are easier to check by word
        wordCheck = list()
        if "Physics" in prospective.getInterests():
            wordCheck.append("Physics")
        if "Chemistry" in prospective.getInterests():
            wordCheck.append("Chemistry")
        if "Biology" in prospective.getInterests():
            wordCheck.append("Biology")
        if "Spanish" in prospective.getInterests():
            wordCheck.append("Spanish")
        if "French" in prospective.getInterests():
            wordCheck.append("French")
        if "Chinese" in prospective.getInterests():
            wordCheck.append("Chinese")
        if "History" in prospective.getInterests():
            wordCheck.append("History")

        artsCheck = list()
        if "2D Visual Arts" in prospective.getArts():
            artsCheck.append("Studio")
        if "Photography" in prospective.getArts():
            artsCheck.append("Photo")
        if "Ceramics" in prospective.getArts():
            artsCheck.append("Ceramics")
        if "Glass" in prospective.getArts():
            artsCheck.append("Glass")
        if "Acting" in prospective.getArts():
            artsCheck.append("Acting")
        if "Theater Tech" in prospective.getArts():
            artsCheck.append("Theater Tech")
        if "Choir/VOX/Singing" in prospective.getArts():
            artsCheck.append("Choir")
        if "Orchestra" in prospective.getArts():
            artsCheck.append("Orchestra")

        schedule = stu.getDaySchedule(time[1], int(time[2]), int(time[3]))
        for course in schedule:
            if course == []:
                continue
            if course[1][0:2] in checkFor and course[1][0:3] != "119":
                toReturn += "\n" + stu.getFirstName() + " is in " + course[0]
                checkFor.remove(course[1][0:2])
            for word in wordCheck:
                if word in course[0]:
                    toReturn += "\n" + stu.getFirstName() + " is in " + course[0]
                    wordCheck.remove(word)
            for art in artsCheck:
                if art in course[0]:
                    toReturn += "\n" + stu.getFirstName() + " is in " + course[0]
                    artsCheck.remove(art)
    return toReturn
    

#if __name__ == "__main__":
#    main()