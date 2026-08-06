import pandas as pd
import numpy as np
from random import choice, seed as set_seed
from src_0118 import task_func
import pytest

def test_task_func_valid_input():
    num_of_students = 10
    df = task_func(num_of_students)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (num_of_students, 4)
    assert list(df.columns) == ['Name', 'Age', 'Gender', 'Score']

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(0)

def test_task_func_seed():
    num_of_students = 10
    seed = 42
    set_seed(seed)
    np.random.seed(seed)
    df1 = task_func(num_of_students, seed=seed)
    set_seed(seed)
    np.random.seed(seed)
    df2 = task_func(num_of_students, seed=seed)
    assert df1.equals(df2)

def test_task_func_name_list():
    num_of_students = 10
    name_list = ['Alice', 'Bob', 'Charlie']
    df1 = task_func(num_of_students, name_list=name_list)
    df2 = task_func(num_of_students)
    assert not df1.equals(df2)

def test_task_func_gender_list():
    num_of_students = 10
    gender_list = ['Male', 'Female']
    df1 = task_func(num_of_students, gender_list=gender_list)
    df2 = task_func(num_of_students)
    assert not df1.equals(df2)

def test_task_func_age_range():
    num_of_students = 10
    age_range = (20, 30)
    df1 = task_func(num_of_students, age_range=age_range)
    df2 = task_func(num_of_students)
    assert not df1.equals(df2)

def test_task_func_score_range():
    num_of_students = 10
    score_range = (0, 100)
    df1 = task_func(num_of_students, score_range=score_range)
    df2 = task_func(num_of_students)
    assert not df1.equals(df2)