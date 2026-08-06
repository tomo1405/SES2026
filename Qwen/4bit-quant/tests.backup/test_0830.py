import pytest
from src_0830 import task_func
import pandas as pd
from statistics import mean

def test_task_func_valid_data():
    data = {
        'Name': ['Alice', 'Bob', 'Alice', 'Charlie'],
        'Score': [85, 92, 78, 88]
    }
    df = pd.DataFrame(data)
    expected_output = {
        'Alice': [('Alice', mean([85, 78]))],
        'Bob': [('Bob', mean([92]))],
        'Charlie': [('Charlie', mean([88]))]
    }
    assert task_func(df) == expected_output

def test_task_func_missing_name_column():
    data = {
        'Score': [85, 92, 78, 88]
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError, match='The DataFram should have the columns "Name" and "Score".'):
        task_func(df)

def test_task_func_missing_score_column():
    data = {
        'Name': ['Alice', 'Bob', 'Alice', 'Charlie']
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError, match='The DataFram should have the columns "Name" and "Score".'):
        task_func(df)

def test_task_func_empty_dataframe():
    df = pd.DataFrame(columns=['Name', 'Score'])
    expected_output = {}
    assert task_func(df) == expected_output

def test_task_func_single_row():
    data = {
        'Name': ['Alice'],
        'Score': [85]
    }
    df = pd.DataFrame(data)
    expected_output = {
        'Alice': [('Alice', mean([85]))]
    }
    assert task_func(df) == expected_output