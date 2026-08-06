import pytest
from src_0153 import task_func
import pandas as pd
import numpy as np

def test_task_func_output_type():
    result = task_func()
    assert isinstance(result, pd.DataFrame), "The output should be a pandas DataFrame."

def test_task_func_columns():
    result = task_func()
    expected_columns = ['Name'] + COURSES + ['Average Grade']
    assert list(result.columns) == expected_columns, "The DataFrame columns do not match the expected columns."

def test_task_func_number_of_rows():
    result = task_func()
    assert len(result) == len(STUDENTS), "The number of rows in the DataFrame should match the number of students."

def test_task_func_student_names():
    result = task_func()
    assert all(name in result['Name'].values for name in STUDENTS), "All student names should be present in the DataFrame."

def test_task_func_course_grades():
    result = task_func()
    for index, row in result.iterrows():
        grades = row[COURSES]
        assert all(isinstance(grade, int) and 0 <= grade <= 100 for grade in grades), "All course grades should be integers between 0 and 100."

def test_task_func_average_grade():
    result = task_func()
    for index, row in result.iterrows():
        grades = row[COURSES]
        average_grade = row['Average Grade']
        calculated_average = np.mean(grades)
        assert np.isclose(average_grade, calculated_average), "The average grade should be correctly calculated."

def test_task_func_randomness():
    result1 = task_func()
    result2 = task_func()
    assert not result1.equals(result2), "The function should generate different results on different calls due to randomness."