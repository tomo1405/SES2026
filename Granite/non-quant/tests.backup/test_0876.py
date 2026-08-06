import pandas as pd
import random
import pytest
from src_0876 import task_func

@pytest.fixture
def input_data():
    return {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, None], 'Occupation': ['Engineer', 'Doctor', 'Teacher']}

def test_task_func_with_seed(input_data):
    seed = 42
    random.seed(seed)
    df = task_func(input_data, fill_missing=True, seed=seed)
    expected_output = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 42], 'Occupation': ['Engineer', 'Doctor', 'Teacher']})
    assert df.equals(expected_output)

def test_task_func_without_seed(input_data):
    df = task_func(input_data, fill_missing=True)
    expected_output = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, random.randint(0, 100)], 'Occupation': ['Engineer', 'Doctor', 'Teacher']})
    assert df.equals(expected_output)

def test_task_func_without_fill_missing(input_data):
    df = task_func(input_data)
    expected_output = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, None], 'Occupation': ['Engineer', 'Doctor', 'Teacher']})
    assert df.equals(expected_output)