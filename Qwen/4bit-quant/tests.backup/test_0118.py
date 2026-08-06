import pytest
from src_0118 import task_func
import pandas as pd
import numpy as np

def test_task_func_with_default_parameters():
    df = task_func(5)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 5
    assert all(df['Name'].isin(['John', 'Mike', 'Sara', 'Emma', 'Nick']))
    assert all(df['Age'].between(15, 20))
    assert all(df['Gender'].isin(['Male', 'Female']))
    assert all(df['Score'].between(50, 100))

def test_task_func_with_custom_name_and_gender_lists():
    df = task_func(3, name_list=['Alice', 'Bob'], gender_list=['Other'])
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 3
    assert all(df['Name'].isin(['Alice', 'Bob']))
    assert all(df['Gender'].isin(['Other']))

def test_task_func_with_custom_age_and_score_ranges():
    df = task_func(4, age_range=(21, 25), score_range=(80, 90))
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 4
    assert all(df['Age'].between(21, 25))
    assert all(df['Score'].between(80, 90))

def test_task_func_with_zero_students():
    with pytest.raises(ValueError):
        task_func(0)

def test_task_func_with_negative_students():
    with pytest.raises(ValueError):
        task_func(-1)

def test_task_func_with_seed():
    df1 = task_func(5, seed=1)
    df2 = task_func(5, seed=1)
    assert df1.equals(df2)