import pytest
from src_0830 import task_func
import pandas as pd
from statistics import mean

def test_task_func_valid_input():
    data = {
        'Name': ['Alice', 'Bob', 'Alice', 'Bob'],
        'Score': [85, 90, 78, 88]
    }
    df = pd.DataFrame(data)
    expected_output = {
        'Alice': iter([('Alice', 81.5)]),
        'Bob': iter([('Bob', 89.0)])
    }
    assert task_func(df) == expected_output

def test_task_func_missing_name_column():
    data = {
        'Score': [85, 90, 78, 88]
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError) as excinfo:
        task_func(df)
    assert str(excinfo.value) == 'The DataFram should have the columns "Name" and "Score".'

def test_task_func_missing_score_column():
    data = {
        'Name': ['Alice', 'Bob', 'Alice', 'Bob']
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError) as excinfo:
        task_func(df)
    assert str(excinfo.value) == 'The DataFram should have the columns "Name" and "Score".'

def test_task_func_empty_dataframe():
    df = pd.DataFrame()
    with pytest.raises(ValueError) as excinfo:
        task_func(df)
    assert str(excinfo.value) == 'The DataFram should have the columns "Name" and "Score".'