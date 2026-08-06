import pytest
from src_0501 import task_func

def test_task_func():
    values = [
        {'ID': 1, 'Name': 'Alice', 'Age': 25},
        {'ID': 2, 'Name': 'Bob', 'Age': 30},
        {'ID': 3, 'Name': 'Charlie', 'Age': 35}
    ]
    filename = 'output.xls'
    expected_output = '/path/to/output.xls'

    actual_output = task_func(values, filename)

    assert actual_output == expected_output