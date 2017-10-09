import student
import pytest
from random import randint

def test_student_creation():
    print('________________TEST STUDENT CREATION__________________')
    student = Student("yves")
    assert student

def setup_for_test():

    name_file = "/Users/yveslym/Desktop/portfolio/MOB2/trip-planner/name.txt"
    fname = open_name_file[random.randint(0, len(open_name_file) - 1)]
    lname = open_name_file[random.randint(0, len(open_name_file) - 1)]

    student = Student(fname+ ' '+lname)
    return student

def test_give_student_assignment():
    '''test adding a new assignment to a student '''
    student = setup_for_test()
    index = 0
    while index < 10:
        course = ['math','chimistry','english','history','computer science','psycology']
        grade_arr = [10,20,30,40,50,60,70,80,90,100]
        index = randint(0,6)
        grade_ind = randint(0,9)
        assignment = course[index]
        grade = grade_arr[grade_ind]
        student.add_assignment(assignment,grade)
        index = index+1
    print('%s final grade %s' %s(student.name,student.grade_in_class))


def test_get_grade_on_assignment():
    '''test retreiving student grade on assignment '''
    student = setup_for_test()

def test_delete_assignment():
    student = setup_for_test()

def test_update_grade_for_assignment():
    '''test updating a grade for a student's assignment '''
    student = setup_for_test()

def test_get_GPA():
    '''tests getting student's average in the class '''
    student = setup_for_test()

def test__update_grade_in_class():
    '''tests helper method _update_grade_in_class().  Any time an assignment and grade are added to a dictionary,
    this method is called.  It recalculates the student's GPA for the class and then updates the value of self.grade_in_class '''
    student = setup_for_test()
