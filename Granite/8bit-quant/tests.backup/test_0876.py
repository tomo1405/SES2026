import pandas as pd
import random
import pytest
from src_0876 import task_func

@pytest.fixture
def input_data():
    return {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, None], 'Occupation': ['Engineer', 'Doctor', 'Teacher']}

def test_task_func_default_args(input_data):
    expected_output = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 50], 'Occupation': ['Engineer', 'Doctor', 'Teacher']})
    output = task_func(input_data)
    assert output.equals(expected_output)

def test_task_func_fill_missing_true(input_data):
    expected_output = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, random.randint(0, 100)], 'Occupation': ['Engineer', 'Doctor', 'Teacher']})
    output = task_func(input_data, fill_missing=True)
    assert output.equals(expected_output)

def test_task_func_num_range(input_data):
    expected_output = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 75], 'Occupation': ['Engineer', 'Doctor', 'Teacher']})
    output = task_func(input_data, fill_missing=True, num_range=(50, 100))
    assert output.equals(expected_output)

def test_task_func_seed(input_data):
    expected_output = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 50], 'Occupation': ['Engineer', 'Doctor', 'Teacher']})
    output_1 = task_func(input_data, seed=123)
    output_2 = task_func(input_data, seed=123)
    assert output_1.equals(output_2)