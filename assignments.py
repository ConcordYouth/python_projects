import student
import records


def enterAssignments():
    print(
        "How would you like to enter assignments? \n 1: By Person \n 2: By Assignment"
    )
    response = records.select_prompt(1, 2)
    match response:
        case 1:
            byPerson()
        case 2:
            byAssignment()
        case _:
            print("enterassignments() broken")


def byPerson():
    studentBeingEdited = records.students[0]
    going = True
    loop1 = True
    loop2 = True
    while going:
        while loop1:
            elementsInStudents = 0
            print("Which person would you like to add assignments to? ")
            for i in range(len(records.students)):
                records.displayStudent(i + 1, records.students[i])
                elementsInStudents += 1
            choiceOfEdit = records.select_prompt(1, elementsInStudents)
            if choiceOfEdit is None:
                print("Exiting...")
                going = False
                loop2 = False
                break
            print(f"Editing {studentBeingEdited.fullname}'s grade sheet. ")
            break

        while loop2:
            assignment = input("What is the name of the assignment?\n> ")
            grade = input(f"What was the received grade for {assignment}?\n> ")
            print("Please verify that the following details are correct (Y/n): ")
            print(f"Assignment: {assignment}")
            print(f"Grade: {grade}")
            correct = records.checkValue("skip")
            if not correct:
                loop1 = False
                break
            else:
                loop1 = True
                data = [assignment, grade]
                studentBeingEdited.assignments.append(data)
                print(
                    f"Would you like to add another assignment to {studentBeingEdited.fullname}'s grade sheet? (Y/n)? "
                )
                goagain = records.checkValue("skip")
                if not goagain:
                    going = False
                    break


def byAssignment():
    pass


def importFiles():
    pass


def exportToFile():
    pass
