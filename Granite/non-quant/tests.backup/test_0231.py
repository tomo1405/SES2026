import pytest
import pandas as pd
from src_0231 import task_func

def test_task_func_invalid_input():
    invalid_input = "Invalid input"
    assert task_func("invalid input") == invalid_input
    assert task_func(123) == invalid_input
    assert task_func([1, 2, 3]) == invalid_input

def test_task_func_valid_input():
    valid_input = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 28, 32],
        'Country': ['USA', 'Canada', 'Japan', 'USA'],
        'Score': [80, 90, 75, 95]
    })
    expected_output = "Invalid input"
    assert task_func(valid_input) != expected_output