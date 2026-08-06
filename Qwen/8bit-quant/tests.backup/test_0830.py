import pytest
from src_0830 import task_func
import pandas as pd
from statistics import mean

def test_task_func_with_valid_data():
    data = {
        'Name': ['Alice', 'Bob', 'Alice', 'Charlie'],
        'Score': [85, 90, 88, 92]
    }
    df = pd.DataFrame(data)
    expected_result = {
        'Alice': iter([('Alice', mean([85, 88]))]),
        'Bob': iter([('Bob', 90)]),
        'Charlie': iter([('Charlie', 92)])
    }
    assert task_func(df) == expected_result

def test_task_func_missing_name_column():
    data = {
        'Score': [85, 90, 88, 92]
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError) as excinfo:
        task_func(df)
    assert str(excinfo.value) == 'The DataFram should have the columns "Name" and "Score".'

def test_task_func_missing_score_column():
    data = {
        'Name': ['Alice', 'Bob', 'Alice', 'Charlie']
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