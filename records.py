import student
from typing import List

students: List[student.Student] = []

michael = student.Student("Michael Mumme", "291961", "michaelmumme@me.com")
students.append(michael)
print(f"length of students = {len(students)}, name = {students[0].fullname}")


def add_students():
    adding = True
    while adding:
        name = ""
        studentID = ""
        email = ""
        check1 = check2 = check3 = check4 = False
        while not check1:
            name = input("What is your full name, First and Last? ")
            check1 = checkValue(name)

        while not check2:
            studentID = input("What is your student ID? ")
            check2 = checkValue(studentID)

        while not check3:
            email = input("What is your email address? ")
            check3 = checkValue(email)
        print("Please verify that the following details are correct (Y/n): ")
        print(f"Name: {name}")
        print(f"Student ID: {studentID}")
        print(f"Email: {email}")
        check4 = checkValue("skip")
        if not check4:
            print("Would you like to reenter? ")
            doItAgain = checkValue("skip")
            if not doItAgain:
                adding = False
        else:
            tempStudent = student.Student(name, studentID, email)
            students.append(tempStudent)
            print("Would you like to enter another student? ")
            doItAgain = checkValue("skip")
            if not doItAgain:
                adding = False


def edit_students():
    editingStudents = True
    while editingStudents:
        elementsInStudents = 0
        for i in range(len(students)):
            print(
                f"{i + 1}: {students[i].fullname}, "
                + f"{students[i].studentID}, {students[i].email}"
            )
            elementsInStudents += 1
        print("Type an index to edit or q to quit. ")
        response = select_prompt(1, elementsInStudents)
        if response is None:
            break
        else:
            response -= 1
            editing(response)


def remove_students():
    removingStudents = True
    while removingStudents:
        if len(students) == 0:
            print("Please add students to the List before trying to remove them.")
            break
        elementsInStudents = 0
        for i in range(len(students)):
            displayStudent(i + 1, students[i])
            elementsInStudents += 1
        print("Type an index to remove or q to quit. ")
        response = select_prompt(
            1, elementsInStudents
        )  ## response based of index + 1, this will be adjusted
        if response is None:
            break
        else:
            print("You're about to delete the following information,")
            print("once completed it CANNOT be undone.")
            displayStudent(response, students[response - 1])
            confirm = checkValue(f"You wish to delete member at index {response}")
            if confirm:
                response -= 1
                students.pop(response)
                if len(students) == 0:
                    print(
                        "You have removed the last student in your library,"
                        + " returning you to the management section"
                    )
                    break


def editing(number: int):
    print(
        "Which property would you like to edit? Name (1),"
        + " Student ID (2), Email (3), Everything (4)"
    )
    answer = select_prompt(1, 4)
    name = students[number].fullname
    studentID = ""
    email = ""
    if answer == 1 or answer == 4:
        while True:
            name = input("Enter full name, first and last: ")
            correct = checkValue(name)
            if correct:
                break
        students[number].fullname = name
    if answer == 2 or answer == 4:
        while True:
            studentID = input(f"Enter {name}'s student ID: ")
            correct = checkValue(studentID)
            if correct:
                break
        students[number].studentID = studentID
    if answer == 3 or answer == 4:
        while True:
            email = input(f"Enter {name}'s email: ")
            correct = checkValue(email)
            if correct:
                break
        students[number].email = email


def select_prompt(min, max):
    number = -10000000000
    while number > max or number < min:
        numberstr = input(">")
        if numberstr == "q":
            return None
        try:
            number = int(numberstr)
        except ValueError:
            print("Please enter an integer")
            continue
        if number > max or number < min:
            print("Option not available.")
        else:
            return int(number)


def checkValue(value):  ## Returns a negative value for someone wanting to continue
    confirm = "y"
    if value != "skip":
        confirm += input(
            f"Please verify that the following is correct (Y/n): {value}\n>"
        ).lower()
    else:
        confirm += input(">")
    confirmation = confirm == "y" or confirm == "yy"
    return confirmation


def displayStudent(index: int, member: student.Student):
    print(f"{index}: {member.fullname}, " + f"{member.studentID}, {member.email}")
