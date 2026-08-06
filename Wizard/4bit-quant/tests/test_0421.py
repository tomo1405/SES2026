python
import pandas as pd
import pytest
from sklearn.preprocessing import StandardScaler
from src_0421 import task_func

def test_task_func():
    # Test case 1: Test with numeric columns
    data = {
        "col1": [1, 2, 3],
        "col2": [4.0, 5.0, 6.0],
        "col3": [7, 8, 9],
        "col4": ["10", "11", "12"],
    }
    expected_result = pd.DataFrame(
        {
            "col1": [-1.224744871391589, 0, 1.224744871391589],
            "col2": [-1.224744871391589, 0, 1.224744871391589],
            "col3": [7, 8, 9],
            "col4": ["10", "11", "12"],
        }
    )
    result = task_func(data)
    assert result.equals(expected_result)

    # Test case 2: Test with non-numeric columns
    data = {
        "col1": [1, 2, 3],
        "col2": ["4.0", "5.0", "6.0"],
        "col3": [7, 8, 9],
        "col4": ["10", "11", "12"],
    }
    expected_result = pd.DataFrame(
        {
            "col1": [1, 2, 3],
            "col2": [4.0, 5.0, 6.0],
            "col3": [7, 8, 9],
            "col4": ["10", "11", "12"],
        }
    )
    result = task_func(data)
    assert result.equals(expected_result)

    # Test case 3: Test with all non-numeric columns
    data = {
        "col1": ["1", "2", "3"],
        "col2": ["4.0", "5.0", "6.0"],
        "col3": ["7", "8", "9"],
        "col4": ["10", "11", "12"],
    }
    expected_result = pd.DataFrame(
        {
            "col1": ["1", "2", "3"],
            "col2": ["4.0", "5.0", "6.0"],
            "col3": ["7", "8", "9"],
            "col4": ["10", "11", "12"],
        }
    )
    result = task_func(data)
    assert result.equals(expected_result)