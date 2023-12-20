from operator import countOf
class Student():

    def __init__(self, email, firstName, lastName, grade, gender,
    middleSchool, dayBoard, town, languages, sportsLFA, sportsNotLFA,
    arts, affinity, clubsMajor, clubsMinor, interests, numVisits):
        # This is the schedule based on the A-day schedule
        # 0 represents no class for G-day
        self.DaySchedule = [[1, 2, 3, 4, 5, 6, 7, 8],
                    [2, 1, 7, 4, 5, 6, 8, 8],
                    [1, 8, 2, 6, 4, 5, 3, 3],
                    [7, 7, 8, 6, 3, 5, 1, 1],
                    [8, 3, 5, 5, 4, 7, 2, 2],
                    [3, 7, 4, 4, 5, 6, 1, 2],
                    [8, 1, 3, 6, 2, 4, 0, 0]]
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.grade = grade
        self.gender = gender
        self.middleSchool = middleSchool
        self.dayBoard = dayBoard
        self.town = town
        self.languages = languages
        self.sportsLFA = sportsLFA
        self.sportsNotLFA = sportsNotLFA
        self.arts = arts
        self.affinity = affinity
        self.clubsMajor = clubsMajor
        self.clubsMinor = clubsMinor
        self.interests = interests
        self.numVisits = numVisits
        self.schedule = [[]*3]*8

    def getEmail(self):
        return self.email
    
    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getGrade(self):
        return self.grade

    def getGender(self):
        return self.gender

    def getMiddleSchool(self):
        return self.middleSchool

    def getDayBoard(self):
        return self.dayBoard

    def getTown(self):
        return self.town

    def getLanguages(self):
        return self.languages

    def getSportsLFA(self):
        return self.sportsLFA

    def getSportsNotLFA(self):
        return self.sportsNotLFA

    def getArts(self):
        return self.arts

    def getAffinity(self):
        return self.affinity

    def getClubsMajor(self):
        return self.clubsMajor

    def getClubsMinor(self):
        return self.clubsMinor

    def getInterests(self):
        return self.interests

    def getSchedule(self):
        return self.schedule

    def getNumVisits(self):
        return self.numVisits

    def getDaySchedule(self, day, start, end):
        sched = self.DaySchedule[ord(day) - ord('A')][start - 1:end]
        return [self.schedule[id - 1] for id in sched]


    def setEmail(self, email):
        self.email = email
    
    def setFirstName(self, firstName):
        self.firstName = firstName

    def setLastName(self, lastName):
        self.lastName = lastName

    def setGrade(self, grade):
        self.grade = grade

    def setGender(self, gender):
        self.gender = gender

    def setMiddleSchool(self, middleSchool):
        self.middleSchool = middleSchool

    def setDayBoard(self, dayBoard):
        self.dayBoard = dayBoard

    def setTown(self, town):
        self.town = town

    def setLanguages(self, languages):
        self.languages = languages

    def setSportsLFA(self, sports):
        self.sportsLFA = sports

    def setSportsNotLFA(self, sports):
        self.sportsNotLFA = sports

    def setArts(self, arts):
        self.arts = arts

    def setAffinity(self, affinity):
        self.affinity = affinity

    def setClubsMajor(self, clubs):
        self.clubsMajor = clubs

    def setClubsMinor(self, clubs):
        self.clubsMinor = clubs

    def setInterests(self, interests):
        self.interests = interests

    def setSchedule(self, schedule):
        self.schedule = schedule

    def setNumVisits(self, numVisits):
        self.numVisits = numVisits

    def setClass(self, name, subject, code, block):
        self.schedule[int(block) - 1] = [name, subject, code]
        for i in range(7):
            if countOf(self.DaySchedule[i], int(block)) > int(code[i]):
                if code[i] == "0":
                    self.DaySchedule[i][self.DaySchedule[i].index(int(block))] = 0
                if code[i] == "1":
                    instance = self.DaySchedule[i].index(int(block))
                    self.DaySchedule[i][self.DaySchedule[i].index(int(block), instance+1)] = 0

    def toString(self):
        print(self.email)
        print(self.firstName)
        print(self.lastName)
        print(self.grade)
        print(self.gender)
        print(self.middleSchool)
        print(self.dayBoard)
        print(self.town)
        print(self.languages)
        print(self.sportsLFA)
        print(self.sportsNotLFA)
        print(self.arts)
        print(self.affinity)
        print(self.clubsMajor)
        print(self.clubsMinor)
        print(self.interests)