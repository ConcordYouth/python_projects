import student
import functions
from typing import List


students: List[student.Student] = []


def Main():
    michael = student.Student("Michael Mumme", "291961", "michaelmumme@me.com")
    students.append(michael)
    while True:
        print("Welcome to Grade Tracker!")
        menu = select_prompt(1, 4, "welcome")
        match menu:
            case 1:
                ManageStudents()
            case 2:
                Grades()
            case 3:
                Files()
            case 4:
                DataAnalytics()
            case _:
                print("case switch broken")


##    michael = student.Student("Michael Mumme", "291961", "michaelmumme@me.com")
##    michael.add_grade("Exam 1", 82.6)
##    avg = michael.calculate_average()
##    print(avg)


def ManageStudents():
    while True:
        option = select_prompt(1, 3, "addstudent")
        match option:
            case 1:
                functions.add_students()
            case 2:
                pass
            case 3:
                pass
            case _:
                print("ManageStudent() broken")


def Grades():
    pass


def Files():
    pass


def DataAnalytics():
    pass


def select_prompt(min, max, menu):
    number = 0
    if menu == "welcome":
        print(
            "__________________________________________________________"
            + "_________________________________________________"
        )
        print(
            "| Manage Student Records (1) | Enter and View Grades (2) |"
            + " Export or Import (3) | View Data Analytics (4) |"
        )
        print(
            "__________________________________________________________"
            + "_________________________________________________"
        )
        print("What would would you like to do? ")
    elif menu == "addstudent":
        print(
            "What would you like to do? \n 1: Add Students"
            + "\n 2: Edit Students \n 3: Remove Students"
        )
    while number > max or number < min:
        numberstr = input(">")
        try:
            number = int(numberstr)
        except ValueError:
            print("Please enter a number")
            continue
        if number > max or number < min:
            print("Option not available.")
        else:
            return number


if __name__ == "__main__":
    Main()
