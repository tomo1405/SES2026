import statistics

import pandas as pd
from src_0851 import task_func


def test_task_func_no_seed():
    students = ['Alice', 'Bob']
    subjects = ['Math', 'Science']
    df = task_func(students, subjects)
    
    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(students)
    assert all(col in df.columns for col in ['Student'] + subjects + ['Average Grade'])
    assert df['Student'].tolist() == students

def test_task_func_with_seed():
    students = ['Alice', 'Bob']
    subjects = ['Math', 'Science']
    seed = 42
    df1 = task_func(students, subjects, seed=seed)
    df2 = task_func(students, subjects, seed=seed)
    
    assert df1.equals(df2), "DataFrames should be equal with the same seed"

def test_task_func_average_grade():
    students = ['Alice']
    subjects = ['Math', 'Science']
    seed = 42
    df = task_func(students, subjects, seed=seed)
    
    grades = df[subjects].iloc[0].tolist()
    expected_avg = statistics.mean(grades)
    assert df['Average Grade'].iloc[0] == expected_avg

def test_task_func_empty_students():
    students = []
    subjects = ['Math', 'Science']
    df = task_func(students, subjects)
    
    assert df.empty

def test_task_func_empty_subjects():
    students = ['Alice', 'Bob']
    subjects = []
    df = task_func(students, subjects)
    
    assert df.empty
    assert df.columns.tolist() == ['Student', 'Average Grade']

def test_task_func_single_student_single_subject():
    students = ['Alice']
    subjects = ['Math']
    seed = 42
    df = task_func(students, subjects, seed=seed)
    
    assert len(df) == 1
    assert len(df.columns) == 3
    assert df['Student'].iloc[0] == 'Alice'
    assert 'Math' in df.columns
    assert 'Average Grade' in df.columns