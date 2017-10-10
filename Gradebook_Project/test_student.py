from student import Student
import pytest
from random import randint
import random

def test_student_creation():
    print('________________TEST STUDENT CREATION__________________')
    student = Student("yves")
    assert student

def setup_for_test():

    name_file = "/Users/yveslym/Desktop/portfolio/MOB2/trip-planner/name.txt"
    open_name_file = open(name_file).read().split()
    fname = open_name_file[random.randint(0, len(open_name_file) - 1)]
    lname = open_name_file[random.randint(0, len(open_name_file) - 1)]

    student = Student(fname+ ' '+lname)
    print('student '+student.name)
    ind = 0
    while ind < 10:
        course = ['math','chimistry','english','history','computer science','psycology']
        grade_arr = [10,20,30,40,50,60,70,80,90,100]
        index = randint(0,5)
        grade_ind = randint(0,8)
        assignment = course[index]
        grade = grade_arr[grade_ind]
        student.add_assignment(assignment,grade)
        print ('assignment '+assignment+' grade '+str(grade))
        ind = ind+1
    return student

# def test_give_student_assignment():
#     '''test adding a new assignment to a student '''
#     student = setup_for_test()




def test_get_grade_on_assignment():
    '''test retreiving student grade on assignment '''
    student = setup_for_test()
    student._update_grade_in_class()
    print(student.name+'grade in class is '+str(student.grade_in_class))

# def test_delete_assignment():
#     student = setup_for_test()
#     student.delete_assignment('Math')

def test_update_grade_for_assignment():
    '''test updating a grade for a student's assignment '''
    student = setup_for_test()
    student.update_grade_for_assignment('English',50)
    student.update_grade_for_assignment('cs1',90)

# def test_get_GPA():
#     '''tests getting student's average in the class '''
#     student = setup_for_test()
#     gpa = student.grade_in_class


def test__update_grade_in_class():
    '''tests helper method _update_grade_in_class().  Any time an assignment and grade are added to a dictionary,
    this method is called.  It recalculates the student's GPA for the class and then updates the value of self.grade_in_class '''
    student = setup_for_test()
    student._update_grade_in_class()
    print('student overall grade: '+str(student.grade_in_class))
