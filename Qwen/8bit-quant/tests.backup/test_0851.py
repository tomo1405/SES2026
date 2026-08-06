import pytest
from src_0851 import task_func
import pandas as pd

def test_task_func_with_seed():
    students = ['Alice', 'Bob']
    subjects = ['Math', 'Science']
    seed = 42
    df = task_func(students, subjects, seed=seed)

    expected_data = [
        ('Alice', 71, 39, 55.0),
        ('Bob', 91, 85, 88.0)
    ]
    expected_df = pd.DataFrame(expected_data, columns=['Student'] + subjects + ['Average Grade'])

    pd.testing.assert_frame_equal(df, expected_df)

def test_task_func_without_seed():
    students = ['Charlie', 'David']
    subjects = ['History', 'Geography']
    df = task_func(students, subjects)

    assert len(df) == 2
    assert len(df.columns) == 4
    assert 'Student' in df.columns
    assert all(subject in df.columns for subject in subjects)
    assert 'Average Grade' in df.columns

def test_task_func_single_student():
    students = ['Eve']
    subjects = ['Art', 'Music']
    df = task_func(students, subjects)

    assert len(df) == 1
    assert len(df.columns) == 4
    assert 'Student' in df.columns
    assert all(subject in df.columns for subject in subjects)
    assert 'Average Grade' in df.columns

def test_task_func_no_subjects():
    students = ['Frank']
    subjects = []
    df = task_func(students, subjects)

    assert len(df) == 1
    assert len(df.columns) == 2
    assert 'Student' in df.columns
    assert 'Average Grade' in df.columns