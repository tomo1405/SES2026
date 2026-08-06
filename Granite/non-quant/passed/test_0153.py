import pandas as pd
import numpy as np
from random import randint
from src_0153 import task_func
import pytest

STUDENTS = ['Joe', 'Amy', 'Mark', 'Sara', 'John', 'Emily', 'Zoe', 'Matt']
COURSES = ['Math', 'Physics', 'Chemistry', 'Biology', 'English', 'History', 'Geography', 'Computer Science']

def test_task_func():
    students_data = []

    for student in STUDENTS:
        grades = [randint(0, 100) for _ in COURSES]
        average_grade = np.mean(grades)
        students_data.append([student] + grades + [average_grade])

    columns = ['Name'] + COURSES + ['Average Grade']
    expected_df = pd.DataFrame(students_data, columns=columns)

    actual_df = task_func()

    assert actual_df.equals(expected_df)