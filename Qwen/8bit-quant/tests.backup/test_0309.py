import pytest
from src_0309 import task_func
import pandas as pd
from statistics import mean
import random

def test_task_func_no_additional_fields():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert all(field in df.columns for field in FIELDS)
    assert 'Average Grade' in df.columns
    assert len(df) == 101  # 100 students + 1 row for averages
    assert len(df.columns) == len(FIELDS) + 2  # original fields + Average Grade + row for averages

def test_task_func_with_additional_fields():
    additional_fields = ['Art', 'Music']
    df = task_func(additional_fields)
    assert isinstance(df, pd.DataFrame)
    assert all(field in df.columns for field in FIELDS + additional_fields)
    assert 'Average Grade' in df.columns
    assert len(df) == 101  # 100 students + 1 row for averages
    assert len(df.columns) == len(FIELDS) + len(additional_fields) + 2  # original fields + additional fields + Average Grade + row for averages

def test_average_grade_calculation():
    df = task_func()
    for student in STUDENTS:
        average_grade = mean(df.loc[student][FIELDS])
        assert df.loc[student]['Average Grade'] == average_grade

def test_subject_average_calculation():
    df = task_func()
    for field in FIELDS:
        subject_average = mean(df[field][STUDENTS])
        assert df.loc['Average'][field] == subject_average

def test_random_grades():
    df1 = task_func()
    df2 = task_func()
    # Check that the grades are different for at least one student in one subject
    assert any(df1.loc[student][field] != df2.loc[student][field] for student in STUDENTS for field in FIELDS)