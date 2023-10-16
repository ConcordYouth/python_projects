import student
from studentIM import students


def add_students():
    adding = True
    while adding:
        name = ""
        studentID = ""
        email = ""
        check1 = check2 = check3 = check4 = True
        while check1:
            name = input("What is your full name, First and Last? ")
            check1 = checkValue(name)

        while check2:
            studentID = input("What is your student ID? ")
            check2 = checkValue(studentID)

        while check3:
            email = input("What is your email address? ")
            check3 = checkValue(email)
        print("Please verify that the following details are correct (Y/n): ")
        print(f"Name: {name}")
        print(f"Student ID {studentID}")
        print(f"Email: {email}")
        check4 = checkValue("skip")
        if check4:
            continue
        else:
            tempStudent = students.Student(name, studentID, email)
            students.append(tempStudent)


def edit_students():
    pass


def remove_students():
    pass


def checkValue(value):
    confirm = "y"
    if value != "skip":
        confirm += input(
            "Please verify that the following information is correct (Y/n):"
            + f" {value}\n>"
        ).lower()
    else:
        confirm += input(">")
    confirmation = confirm == "y" or confirm == "yy"
    return not confirmation
