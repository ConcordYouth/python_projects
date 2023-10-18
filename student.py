from typing import List


class Student:
    def __init__(self, name, Identification, contact):
        self.fullname = name
        self.studentID = Identification
        self.email = contact
        self.assignments: List[List[str]] = []

    def add_grade(self, assignment, grade):
        self.assignments[assignment] = grade

    def calculate_average(self):
        total = 0
        i = 0


##        for grade in self.assignments.values():
##            total += grade
##            i += 1
##        return total / i
