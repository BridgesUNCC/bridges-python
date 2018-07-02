
class Student:


    def __init__(self, id, name, study, email, likeColor, dislikeColor, creditHours):
        self.id = id
        self.name = name
        self.study = study
        self.email = email
        self.likeColor = likeColor
        self.dislikeColor = dislikeColor
        self.creditHours = creditHours

    def getid(self):
        return self.id
    def getName(self):
        return self.name
    def getStudy(self):
        return self.study
    def getEmail(self):
        return self.email
    def getLikeColor(self):
        return self.likeColor
    def getDislikeColor(self):
        return self.dislikeColor
    def getCreditHours(self):
        return self.creditHours
