import pandas as pd
import random
import pytest

from src_0876 import task_func

@pytest.fixture
def input_data():
    return {'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [25, 30, None],
            'Occupation': ['Engineer', 'Doctor', 'Teacher']}

def test_task_func(input_data):
    df = task_func(input_data)
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ['Name', 'Age', 'Occupation']
    assert df['Age'].dtype == 'Int64'
    assert df['Occupation'].dtype == 'object'

def test_task_func_fill_missing(input_data):
    df = task_func(input_data, fill_missing=True)
    assert df['Age'].dtype == 'Int64'
    assert df['Age'].isnull().sum() == 1

def test_task_func_seed(input_data):
    df1 = task_func(input_data, seed=123)
    df2 = task_func(input_data, seed=123)
    assert df1.equals(df2)

def test_task_func_invalid_column(input_data):
    with pytest.raises(ValueError, match='Invalid column'):
        task_func(input_data, columns=['Invalid'])

def test_task_func_invalid_num_range(input_data):
    with pytest.raises(ValueError, match='Invalid number range'):
        task_func(input_data, num_range=(100, 0))