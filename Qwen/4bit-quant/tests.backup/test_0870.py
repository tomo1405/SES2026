import pytest
from src_0870 import task_func
import pandas as pd

def test_task_func_with_default_parameters():
    df = task_func(5)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (5, 2)
    assert all(df.columns == ['Student', 'Grade'])
    assert all(df['Student'].isin(['Alice', 'Bob', 'Charlie', 'David', 'Eve']))

def test_task_func_with_custom_students():
    students = ['Tom', 'Jerry']
    df = task_func(4, students=students)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (4, 2)
    assert all(df.columns == ['Student', 'Grade'])
    assert all(df['Student'].isin(students))

def test_task_func_with_custom_grade_range():
    grade_range = range(6, 10)
    df = task_func(3, grade_range=grade_range)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 2)
    assert all(df.columns == ['Student', 'Grade'])
    assert all(df['Grade'].between(min(grade_range), max(grade_range)))

def test_task_func_with_rng_seed():
    seed_value = 42
    df1 = task_func(3, rng_seed=seed_value)
    df2 = task_func(3, rng_seed=seed_value)
    assert df1.equals(df2)

def test_task_func_with_zero_grades():
    with pytest.raises(ValueError):
        task_func(0)

def test_task_func_with_empty_students_list():
    with pytest.raises(ValueError):
        task_func(5, students=[])

def test_task_func_with_single_student():
    students = ['OnlyOne']
    df = task_func(5, students=students)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (5, 2)
    assert all(df.columns == ['Student', 'Grade'])
    assert all(df['Student'] == students[0])