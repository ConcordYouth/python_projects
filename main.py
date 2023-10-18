import records
import assignments


def Main():
    print("Welcome to Grade Tracker!")
    while True:
        DisplayMenu()
        menu = records.select_prompt(1, 3)
        if menu == "q":
            print("Thank You for Using Grade Tracker!")
            break
        match menu:
            case 1:
                ManageStudents()
            case 2:
                Grades()
            case 3:
                DataAnalytics()
            case _:
                print("case switch broken")


def ManageStudents():
    while True:
        print(
            "What would you like to do? \n 1: Add Students"
            + "\n 2: Edit Students \n 3: Remove Students"
        )
        print("Or type 'q' to quit")
        option = records.select_prompt(1, 3)
        if option is None:
            break
        match option:
            case 1:
                records.add_students()
            case 2:
                records.edit_students()
            case 3:
                records.remove_students()
            case _:
                print("ManageStudent() broken")


def Grades():
    while True:
        print(
            "What would you like to do? \n 1: Enter Grades"
            + "\n 2: Import Grades \n 3: Export Grades"
        )
        print("Or type 'q' to quit")
        option = records.select_prompt(1, 3)
        if option is None:
            break
        match option:
            case 1:
                assignments.enterAssignments()
            case 2:
                assignments.importFiles()
            case 3:
                assignments.exportToFile()
            case _:
                print("Grades() broken")


def DataAnalytics():
    pass


def DisplayMenu():
    print(
        "__________________________________________________________"
        + "___________________________"
    )
    print(
        "| Manage Student Records (1) | Enter and View Grades (2) |"
        + "  View Data Analytics (3) |"
    )
    print(
        "__________________________________________________________"
        + "___________________________"
    )
    print("What would would you like to do? ")


if __name__ == "__main__":
    Main()
