import pytest
from src_0876 import task_func
import pandas as pd
import random

def test_task_func_with_valid_input():
    data = [
        {'Name': 'Alice', 'Age': 30, 'Occupation': 'Doctor'},
        {'Name': 'Bob', 'Age': 25, 'Occupation': 'Engineer'},
        {'Name': 'Charlie', 'Age': 40, 'Occupation': 'Teacher'}
    ]
    columns = ['Name', 'Age', 'Occupation']
    fill_missing = False
    num_range = (0, 100)
    seed = None

    expected_output = pd.DataFrame(data, columns=columns)

    output = task_func(data, columns, fill_missing, num_range, seed)

    pd.testing.assert_frame_equal(output, expected_output)

def test_task_func_with_invalid_input():
    data = [
        {'Name': 'Alice', 'Age': 30, 'Occupation': 'Doctor'},
        {'Name': 'Bob', 'Age': 25, 'Occupation': 'Engineer'},
        {'Name': 'Charlie', 'Age': 40, 'Occupation': 'Teacher'}
    ]
    columns = ['Name', 'Age', 'Occupation']
    fill_missing = False
    num_range = (0, 100)
    seed = None

    with pytest.raises(ValueError):
        task_func(data, columns, fill_missing, num_range, seed)

def test_task_func_with_valid_input_and_fill_missing():
    data = [
        {'Name': 'Alice', 'Age': 30, 'Occupation': 'Doctor'},
        {'Name': 'Bob', 'Age': 25, 'Occupation': 'Engineer'},
        {'Name': 'Charlie', 'Age': 40, 'Occupation': 'Teacher'}
    ]
    columns = ['Name', 'Age', 'Occupation']
    fill_missing = True
    num_range = (0, 100)
    seed = None

    expected_output = pd.DataFrame(data, columns=columns)

    output = task_func(data, columns, fill_missing, num_range, seed)

    pd.testing.assert_frame_equal(output, expected_output)

def test_task_func_with_invalid_input_and_fill_missing():
    data = [
        {'Name': 'Alice', 'Age': 30, 'Occupation': 'Doctor'},
        {'Name': 'Bob', 'Age': 25, 'Occupation': 'Engineer'},
        {'Name': 'Charlie', 'Age': 40, 'Occupation': 'Teacher'}
    ]
    columns = ['Name', 'Age', 'Occupation']
    fill_missing = True
    num_range = (0, 100)
    seed = None

    with pytest.raises(ValueError):
        task_func(data, columns, fill_missing, num_range, seed)