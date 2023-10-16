import student
import functions


def Main():
    print("Welcome to Grade Tracker!")
    while True:
        DisplayMenu()
        menu = functions.select_prompt(1, 4)
        if menu == "q":
            print("Thank You for Using Grade Tracker!")
            break
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
        print(
            "What would you like to do? \n 1: Add Students"
            + "\n 2: Edit Students \n 3: Remove Students"
        )
        print("Or type 'q' to quit")
        option = functions.select_prompt(1, 3)
        if option is None:
            break
        match option:
            case 1:
                functions.add_students()
            case 2:
                functions.edit_students()
            case 3:
                functions.remove_students()
            case _:
                print("ManageStudent() broken")


def Grades():
    pass


def Files():
    pass


def DataAnalytics():
    pass


def DisplayMenu():
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


if __name__ == "__main__":
    Main()
