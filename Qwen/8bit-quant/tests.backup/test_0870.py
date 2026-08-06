import pytest
from src_0870 import task_func
import pandas as pd

def test_task_func_no_students():
    with pytest.raises(ValueError):
        task_func(n_grades=5, students=[])

def test_task_func_default_parameters():
    df = task_func(n_grades=10)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 10
    assert all(df['Student'].isin(['Alice', 'Bob', 'Charlie', 'David', 'Eve']))
    assert all(df['Grade'].between(1, 10))

def test_task_func_custom_students():
    students = ['Tom', 'Jerry']
    df = task_func(n_grades=4, students=students)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 4
    assert all(df['Student'].isin(students))
    assert all(df['Grade'].between(1, 10))

def test_task_func_custom_grade_range():
    grade_range = range(5, 10)
    df = task_func(n_grades=6, grade_range=grade_range)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 6
    assert all(df['Grade'].between(5, 9))

def test_task_func_with_seed():
    df1 = task_func(n_grades=3, rng_seed=42)
    df2 = task_func(n_grades=3, rng_seed=42)
    assert df1.equals(df2)

def test_task_func_zero_grades():
    df = task_func(n_grades=0)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 0