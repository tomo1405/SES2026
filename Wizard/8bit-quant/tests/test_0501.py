python
import pytest
from src_0501 import task_func

# Constants
FIELDS = ['ID', 'Name', 'Age']

def test_task_func():
    # Test case 1
    values = [
        {'ID': 1, 'Name': 'John', 'Age': 30},
        {'ID': 2, 'Name': 'Jane', 'Age': 25},
        {'ID': 3, 'Name': 'Bob', 'Age': 40}
    ]
    filename = 'test.xls'
    expected_result = os.path.abspath(filename)
    result = task_func(values, filename)
    assert result == expected_result

    # Test case 2
    values = [
        {'ID': 1, 'Name': 'John', 'Age': 30},
        {'ID': 2, 'Name': 'Jane', 'Age': 25},
        {'ID': 3, 'Name': 'Bob', 'Age': 40}
    ]
    filename = 'test.xlsx'
    expected_result = os.path.abspath(filename)
    result = task_func(values, filename)
    assert result == expected_result

    # Test case 3
    values = [
        {'ID': 1, 'Name': 'John', 'Age': 30},
        {'ID': 2, 'Name': 'Jane', 'Age': 25},
        {'ID': 3, 'Name': 'Bob', 'Age': 40}
    ]
    filename = 'test.txt'
    expected_result = os.path.abspath(filename)
    result = task_func(values, filename)
    assert result == expected_result

    # Test case 4
    values = [
        {'ID': 1, 'Name': 'John', 'Age': 30},
        {'ID': 2, 'Name': 'Jane', 'Age': 25},
        {'ID': 3, 'Name': 'Bob', 'Age': 40}
    ]
    filename = 'test.csv'
    expected_result = os.path.abspath(filename)
    result = task_func(values, filename)
    assert result == expected_result

    # Test case 5
    values = [
        {'ID': 1, 'Name': 'John', 'Age': 30},
        {'ID': 2, 'Name': 'Jane', 'Age': 25},
        {'ID': 3, 'Name': 'Bob', 'Age': 40}
    ]
    filename = 'test.pdf'
    expected_result = os.path.abspath(filename)
    result = task_func(values, filename)
    assert result == expected_result