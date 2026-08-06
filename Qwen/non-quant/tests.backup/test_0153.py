import pytest
from src_0153 import task_func
import pandas as pd
import numpy as np

def test_task_func_columns():
    df = task_func()
    expected_columns = ['Name'] + ['Math', 'Physics', 'Chemistry', 'Biology', 'English', 'History', 'Geography', 'Computer Science'] + ['Average Grade']
    assert list(df.columns) == expected_columns

def test_task_func_number_of_rows():
    df = task_func()
    assert len(df) == len(STUDENTS)

def test_task_func_student_names():
    df = task_func()
    assert all(name in df['Name'].values for name in STUDENTS)

def test_task_func_grades_range():
    df = task_func()
    for index, row in df.iterrows():
        grades = row[COURSES]
        assert all(0 <= grade <= 100 for grade in grades)

def test_task_func_average_grade():
    df = task_func()
    for index, row in df.iterrows():
        grades = row[COURSES]
        average_grade = np.mean(grades)
        assert np.isclose(row['Average Grade'], average_grade)

def test_task_func_data_types():
    df = task_func()
    assert df['Name'].dtype == object
    for course in COURSES:
        assert df[course].dtype == np.int64
    assert df['Average Grade'].dtype == np.float64