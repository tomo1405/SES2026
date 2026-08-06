import pandas as pd
import pytest
from src_0887 import task_func


def test_task_func():
    data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'Score': [90, 80, 70]}
    df, avg_scores, most_common_age = task_func(data)

    assert df.equals(pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'Score': [90, 80, 70]}).sort_values(['Name', 'Age']))
    assert avg_scores.equals(pd.Series([90, 80, 70], index=['Alice', 'Bob', 'Charlie']))
    assert most_common_age == 30

def test_task_func_missing_key():
    data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'Score': [90, 80, 70]}
    with pytest.raises(ValueError):
        task_func(data, 'Name')

def test_task_func_invalid_key():
    data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'Score': [90, 80, 70]}
    with pytest.raises(ValueError):
        task_func(data, 'Invalid')

def test_task_func_empty_data():
    data = {}
    with pytest.raises(ValueError):
        task_func(data)

def test_task_func_invalid_data():
    data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'Score': [90, 80, 70]}
    with pytest.raises(ValueError):
        task_func(data, 'Invalid')