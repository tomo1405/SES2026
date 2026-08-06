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
        assert all(df[field].apply(lambda x: 0 <= x <= 100))
    average_grades = df['Average Grade']
    for student in STUDENTS:
        assert average_grades[student] == mean(df.loc[student])
    assert average_grades['Average'] == mean(df.loc['Average'])

def test_task_func_additional_fields():
    additional_fields = ['Geography', 'Physics']
    df = task_func(additional_fields)
    assert list(df.columns) == FIELDS + additional_fields + ['Average Grade']