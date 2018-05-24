

class Student():
    studentID = str()
    fullName = str()
    program = str()
    email = str()
    dislikeColor = str()
    favoriteColor = str()
    studentCreditHours = float()

    def __init__(self, studentID, fullName, program, email, dislikeColor, favoriteColor, studentCreditHours):
        self.studentID = studentID
        self.fullName = fullName
        self.program = program
        self.email = email
        self.dislikeColor = dislikeColor
        self.favoriteColor = favoriteColor
        self.studentCreditHours = studentCreditHours