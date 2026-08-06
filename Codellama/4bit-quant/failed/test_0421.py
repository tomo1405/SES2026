import pytest
from src_0421 import task_func

def test_task_func():
    # Test case 1: Test with a dataframe containing only numeric columns
    data = {
        "column1": [1, 2, 3, 4, 5],
        "column2": [10, 20, 30, 40, 50],
        "column3": [100, 200, 300, 400, 500]
    }
    expected_output = {
        "column1": [0.0, 1.0, 2.0, 3.0, 4.0],
        "column2": [0.0, 1.0, 2.0, 3.0, 4.0],
        "column3": [0.0, 1.0, 2.0, 3.0, 4.0]
    }
    output = task_func(data)
    assert output.equals(expected_output)

    # Test case 2: Test with a dataframe containing non-numeric columns
    data = {
        "column1": [1, 2, 3, 4, 5],
        "column2": [10, 20, 30, 40, 50],
        "column3": ["a", "b", "c", "d", "e"]
    }
    expected_output = {
        "column1": [0.0, 1.0, 2.0, 3.0, 4.0],
        "column2": [0.0, 1.0, 2.0, 3.0, 4.0],
        "column3": ["a", "b", "c", "d", "e"]
    }
    output = task_func(data)
    assert output.equals(expected_output)

    # Test case 3: Test with a dataframe containing a mix of numeric and non-numeric columns
    data = {
        "column1": [1, 2, 3, 4, 5],
        "column2": [10, 20, 30, 40, 50],
        "column3": ["a", "b", "c", "d", "e"],
        "column4": [100, 200, 300, 400, 500]
    }
    expected_output = {
        "column1": [0.0, 1.0, 2.0, 3.0, 4.0],
        "column2": [0.0, 1.0, 2.0, 3.0, 4.0],
        "column3": ["a", "b", "c", "d", "e"],
        "column4": [0.0, 1.0, 2.0, 3.0, 4.0]
    }
    output = task_func(data)
    assert output.equals(expected_output)