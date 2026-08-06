import pytest
from src_0919 import task_func

def test_task_func():
    data = {'Name': ['John Doe', 'Jane Doe'], 'Age': [25, 30], 'City': ['New York', 'London']}
    mapping = {'NY': 'New York', 'LDN': 'London'}
    expected_output = {'Name': ['John Doe', 'Jane Doe'], 'Age': [25, 30], 'City': ['New York', 'London']}
    assert task_func(data, mapping).equals(expected_output)

def test_task_func_with_invalid_input():
    data = {'Name': ['John Doe', 'Jane Doe'], 'Age': [25, 30], 'City': ['New York', 'London']}
    mapping = {'NY': 'New York', 'LDN': 'London'}
    with pytest.raises(ValueError):
        task_func(data, mapping, invalid_input)