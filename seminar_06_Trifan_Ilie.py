"""
Write an application that manages a group of students.
Each student has a unique id (string), a name (string) and a grade (integer).
The application will have a menu-driven user interface and will provide the
following features:

    1. Add a student
        - adds the student with the given id, name and grade to the list.
        - error if giving existing id, the name or grade fields not given or
        empty

    2. Delete a student
        - deletes the student with the given id from the list
        - error if non-existing id given

    3. Show all students
        - shows all students in descending order of their grade

    4. Show students whose grade is > than given one, ordered in descending
    order of grade

    5. exit
        - exit the program

    Observations:
        - Add 10 random students at program startup
        - Write specifications for non-UI functions
        - Each function does one thing only, and communicates via parameters and return value
        - The program reports errors to the user. It must also report errors from non-UI functions!
        - Make sure you understand the student's representation
        - Try to reuse functions across functionalities (Less code to write and test)
        - Don't use global variables!
"""

import random
#
# Write the implementation for Seminar 06 in this file
#

#
# Write below this comment
# Functions to deal with students -- list representation
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#

# 9981, Popescu Ioana, 10 => ["9981", "Popescu Ioana", 10]
def create_student(id, name: str, grade: int):
    """
    Create a new student
    :return: The new student, or None if any of the fields are empty
    """
    if(id and name and grade):
        return [id, name, grade]
    else:
        return None
    pass


def get_id(student):
    return student[0]


def get_name(student):
    return student[1]


def get_grade(student):
    return student[2]


def to_str(student):
    """
    Return the str representation of the student
    :param student: Given student
    :return: For student 9981, Popescu Ioana, 10, return
    "id: 9981; name: Popescu Ioana has grade 10"
    """
    return "id:"+get_id((student))+"; name:"+get_name(student)+"has grade "+get_grade(student)


#
# Write below this comment
# Functions to deal with students -- dict representation
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
# TODO Copy the exact function signatures from previous block and implement
# them as dict

# 9981, Popescu Ioana, 10 => {"id": "9981","name": "Popescu Ioana","grade": 10}

#
# Write below this comment
# Functions that deal with the required functionalities properties
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
def generate_students(count: int):
    family_name = ['Popescu', 'Marian', 'Pop', 'Lazarescu', 'Dincu']
    given_name = ['Anca', 'Emilia', 'Liviu', 'Marius']

    student_list = []

    while count > 0:
        family = random.choice(family_name)
        given = random.choice(given_name)
        full_name = family + " " + given

        student = create_student(str(9000 + count), full_name, random.randint(4, 10))
        student_list.append(student)
        count -= 1
    return student_list

def add_student(student_list : list, new_student):
    """
    Add the new student to the list
    :param student_list: The list of all students in the program
    :param new_student: The new guy
    :return: 0 on success, 1 if duplicate student id
    """
    for student in range(0,len(student_list)):
        if get_id(student_list[student]) == get_id(new_student):
            return 1
    student_list.append(new_student)
    return 0

def show_list(student_list: list):
    return student_list

def delete_student(student_list,idToBeDeleted):
    for student in range(0,len(student_list)):
        if(get_id(student_list[student])==idToBeDeleted):
            student_list.pop(student)
            return 0
    return 1

def show_good_grades(student_list, grade):
    good_grade_students= []
    for student in student_list:
        if get_grade(student)>grade:
            add_student(good_grade_students)
    good_grade_students.sort(reverse= True, key= lambda x: x[2])

#
# Write below this comment
# UI section
# Write all functions that have input or print statements here
# Ideally, this section should not contain any calculations relevant to program functionalities
#
def start():
    # TODO What do we need here?
    # 1. Print main menu
    # 2. Read user choice -> call appropriate function
    # 3. Print out any error message
    # 4. Exit !?
    student_list = generate_students(5)
    while True:
        print("1. Create new Student\n", "2. Delete Student\n", "3. Show Students\n", "4. Order grade descending\n", "0. Exit !?")
        option=input("Choose an option:")
        if option == "0":
            break
        elif option == "1":
            id= input("id:")
            name = input("Name:")
            grade = int(input("Grade:"))
            add_student(student_list, create_student(id, name, grade))
        elif option == "2":
            id= input("id:")
            if(delete_student(student_list,id)==1):
                print("Student was not found")
        elif option == "3":
            print("Here is the list:",show_list(student_list))
        elif option == "4":
            grade= int(input("Grade:"))
            show_good_grades(student_list, grade)
        else: print("Bad input, please try again.")


if __name__ == "__main__":

    start()
