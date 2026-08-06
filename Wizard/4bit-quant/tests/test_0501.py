python
import pytest
from src_0501 import task_func

# Constants
FIELDS = ['ID', 'Name', 'Age']

# Test case 1
def test_task_func_valid_data():
    values = [
        {'ID': 1, 'Name': 'John', 'Age': 25},
        {'ID': 2, 'Name': 'Jane', 'Age': 30},
        {'ID': 3, 'Name': 'Bob', 'Age': 40},
    ]
    filename = 'test.xls'
    expected_result = os.path.abspath(filename)

    result = task_func(values, filename)

    assert result == expected_result
    assert os.path.exists(filename)
    os.remove(filename)

# Test case 2
def test_task_func_invalid_data():
    values = [
        {'ID': 1, 'Name': 'John', 'Age': 25},
        {'ID': 2, 'Name': 'Jane', 'Age': 'invalid'},
        {'ID': 3, 'Name': 'Bob', 'Age': 40},
    ]
    filename = 'test.xls'
    expected_result = os.path.abspath(filename)

    result = task_func(values, filename)

    assert result == expected_result
    assert os.path.exists(filename)
    os.remove(filename)

# Test case 3
def test_task_func_empty_data():
    values = []
    filename = 'test.xls'
    expected_result = os.path.abspath(filename)

    result = task_func(values, filename)

    assert result == expected_result
    assert os.path.exists(filename)
    os.remove(filename)