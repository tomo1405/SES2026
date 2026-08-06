python
import pandas as pd
import numpy as np
from random import randint
import pytest

# Constants
STUDENTS = ['Joe', 'Amy', 'Mark', 'Sara', 'John', 'Emily', 'Zoe', 'Matt']
COURSES = ['Math', 'Physics', 'Chemistry', 'Biology', 'English', 'History', 'Geography', 'Computer Science']

def task_func():
    students_data = []

    for student in STUDENTS:
        grades = [randint(0, 100) for _ in COURSES]
        average_grade = np.mean(grades)
        students_data.append([student] + grades + [average_grade])

    columns = ['Name'] + COURSES + ['Average Grade']
    grades_df = pd.DataFrame(students_data, columns=columns)

    return grades_df

def test_task_func():
    grades_df = task_func()
    assert isinstance(grades_df, pd.DataFrame)
    assert grades_df.shape == (8, 9)
    assert grades_df.columns.tolist() == ['Name', 'Math', 'Physics', 'Chemistry', 'Biology', 'English', 'History', 'Geography', 'Computer Science', 'Average Grade']
    assert grades_df['Name'].tolist() == STUDENTS
    for course in COURSES:
        assert grades_df[course].dtype == 'int64'
    assert grades_df['Average Grade'].dtype == 'float64'
    assert grades_df['Average Grade'].mean() == pytest.approx(70.0, 0.1)