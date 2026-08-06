import pytest
from src_0309 import task_func
import pandas as pd
import numpy as np

def test_task_func_default_fields():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert len(df.columns) == 7  # 6 fields + 1 'Average Grade'
    assert len(df.index) == 101  # 100 students + 1 'Average' row
    assert all(field in df.columns for field in ['Physics', 'Math', 'Chemistry', 'Biology', 'English', 'History'])

def test_task_func_additional_fields():
    additional_fields = ['Art', 'Music']
    df = task_func(additional_fields)
    assert isinstance(df, pd.DataFrame)
    assert len(df.columns) == 9  # 6 default fields + 2 additional fields + 1 'Average Grade'
    assert len(df.index) == 101  # 100 students + 1 'Average' row
    assert all(field in df.columns for field in ['Physics', 'Math', 'Chemistry', 'Biology', 'English', 'History', 'Art', 'Music'])

def test_task_func_student_average_grades():
    df = task_func()
    assert all(isinstance(avg, float) for avg in df['Average Grade'])

def test_task_func_subject_averages():
    df = task_func()
    subject_averages = df.loc['Average']
    assert all(isinstance(avg, float) for avg in subject_averages)

def test_task_func_random_grades_range():
    df = task_func()
    for column in df.columns[:-1]:  # Exclude 'Average Grade' column
        grades = df[column]
        assert all(0 <= grade <= 100 for grade in grades)

def test_task_func_random_grades_distribution():
    np.random.seed(0)  # For reproducibility
    df = task_func()
    for column in df.columns[:-1]:  # Exclude 'Average Grade' column
        grades = df[column]
        assert np.allclose(np.mean(grades), 54.88, atol=1)  # Approximate mean due to randomness

def test_task_func_average_grade_calculation():
    np.random.seed(0)  # For reproducibility
    df = task_func()
    for index, row in df.iterrows():
        if index != 'Average':
            assert np.isclose(row['Average Grade'], np.mean(row[:-1]), atol=1)

def test_task_func_subject_average_calculation():
    np.random.seed(0)  # For reproducibility
    df = task_func()
    for column in df.columns[:-1]:  # Exclude 'Average Grade' column
        assert np.isclose(df.loc['Average', column], np.mean(df[column][:-1]), atol=1)