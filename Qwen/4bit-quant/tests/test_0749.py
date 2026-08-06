import pytest
from src_0749 import task_func
import pandas as pd
from sklearn.preprocessing import StandardScaler

def test_task_func_empty_input():
    df = pd.DataFrame({'Age': [30, 25, 40], 'Weight': [70, 60, 80]})
    age = 20
    weight = 90
    result = task_func(df, age, weight)
    assert result.empty

def test_task_func_non_empty_input():
    df = pd.DataFrame({'Age': [30, 25, 40], 'Weight': [70, 60, 80]})
    age = 35
    weight = 50
    result = task_func(df, age, weight)
    assert not result.empty
    assert all(result.columns == ['Age', 'Weight'])
    assert isinstance(result, pd.DataFrame)

def test_task_func_standardization():
    df = pd.DataFrame({'Age': [30, 25, 40], 'Weight': [70, 60, 80]})
    age = 35
    weight = 50
    result = task_func(df, age, weight)
    scaler = StandardScaler()
    expected = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
    assert result.equals(expected)

def test_task_func_column_names():
    df = pd.DataFrame({'Age': [30, 25, 40], 'Weight': [70, 60, 80]})
    age = 35
    weight = 50
    result = task_func(df, age, weight)
    assert list(result.columns) == ['Age', 'Weight']

def test_task_func_with_zero_variance():
    df = pd.DataFrame({'Age': [30, 30, 30], 'Weight': [70, 70, 70]})
    age = 35
    weight = 50
    result = task_func(df, age, weight)
    assert result.empty

def test_task_func_with_single_row():
    df = pd.DataFrame({'Age': [20], 'Weight': [70]})
    age = 25
    weight = 60
    result = task_func(df, age, weight)
    assert result.empty

def test_task_func_with_multiple_rows():
    df = pd.DataFrame({'Age': [20, 22, 24], 'Weight': [70, 72, 74]})
    age = 25
    weight = 71
    result = task_func(df, age, weight)
    assert len(result) == 2