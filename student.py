class Student:
    def __init__(self, name, Identification, contact):
        self.fullname = name
        self.studentID = Identification
        self.email = contact
        self.grades = {}

    def add_grade(self, assignment, grade):
        self.grades[assignment] = grade

    def calculate_average(self):
        total = 0
        i = 0
        for grade in self.grades.values():
            total += grade
            i += 1
        return total / i
