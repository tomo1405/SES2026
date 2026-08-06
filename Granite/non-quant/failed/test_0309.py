import pandas as pd
from statistics import mean
import random
from src_0309 import task_func

FIELDS = ['Physics', 'Math', 'Chemistry', 'Biology', 'English', 'History']
STUDENTS = ['Student_' + str(i) for i in range(1, 101)]

def test_task_func():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert list(df.index) == STUDENTS
    assert list(df.columns) == FIELDS + ['Average Grade']
    for field in FIELDS:
        assert all(isinstance(grade, int) for grade in df[field])
    average_grades = df['Average Grade']
    assert all(isinstance(grade, float) for grade in average_grades)
    assert all(grade >= 0 and grade <= 100 for grade in average_grades)

def test_task_func_additional_fields():
    additional_fields = ['Geography', 'Physics']
    df = task_func(additional_fields)
    assert list(df.columns) == FIELDS + additional_fields + ['Average Grade']