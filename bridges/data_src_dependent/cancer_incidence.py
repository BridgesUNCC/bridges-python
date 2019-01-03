
class CancerIncidence:

    def __init__(self):
        self.loc = []
        self.year = 0
        self.count = 0
        self.population = 0
        self.gender = ""
        self.race = ""
        self.event_type = ""
        self.affected_area = ""
        self.ageAdjustedRate = 0.0
        self.crudeRate = 0.0
        self.loc.append(0.0)
        self.loc.append(0.0)
        self.ageAdjustedRateci= []
        self.crudeRateci = []
        self.ageAdjustedRateci.append(0.0)
        self.ageAdjustedRateci.append(0.0)
        self.crudeRateci.append(0.0)
        self.crudeRateci.append(0.0)

    def getAgeAdjustedRate(self):
        return self.ageAdjustedRate
    def setAgeAdjustedRate(self, arr):
        self.ageAdjustedRate = arr

    def getAgeAdjustedCI_Lower(self):
        return self.ageAdjustedRateci[0]
    def setAgeAdjustedCI_Lower(self, ci_l):
        self.ageAdjustedRateci[0] = ci_l

    def getAgeAdjustedCI_Upper(self):
        return self.ageAdjustedRateci[1]
    def setAgeAdjustedCI_Upper(self, ci_u):
        self.ageAdjustedRateci[1] = ci_u

    def getCrudeRate(self):
        return self.crudeRate
    def setCrudeRate(self, cr):
        self.crudeRate = cr

    def getCrudeRate_CI_Lower(self):
        return self.crudeRateci[0]
    def setCrudeRate_CI_lower(self, cr_l):
        self.crudeRateci[0] = cr_l

    def getCrudeRate_CI_Upper(self):
        return self.crudeRateci[1]

    def setCrudeRate_CI_Upper(self, cr_l):
        self.crudeRateci[1] = cr_l

    def getYear(self):
        return self.year
    def setYear(self, year):
        self.year = year

    def getGender(self):
        return self.gender
    def setGender(self, gender):
        self.gender = gender

    def getRace(self):
        return self.race
    def setRace(self, race):
        self.race = race

    def getEventType(self):
        return self.event_type
    def setEventType(self, et):
        self.event_type = et

    def getPopulation(self):
        return self.population
    def setPopulation(self, pop):
        self.population = pop

    def getAffectedArea(self):
        return self.affected_area
    def setAffectedArea(self, area):
        self.affected_area = area

    def getCount(self):
        return self.count
    def setCount(self,count):
        self.count = count

    def getLocationX(self):
        return self.loc[0]
    def setLocationX(self, x):
        self.loc[0] = x

    def getLocationY(self):
        return self.loc[1]
    def setLocationY(self, y):
        self.loc[1] = y
