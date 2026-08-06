python
import pandas as pd
import pytest
from sklearn.preprocessing import StandardScaler
from src_0421 import task_func

def test_task_func():
    # Test case 1: Test with a dataframe with numeric columns
    data = {"col1": [1, 2, 3], "col2": [4, 5, 6], "col3": [7, 8, 9]}
    dataframe = pd.DataFrame(data)
    expected_result = pd.DataFrame(
        {"col1": [-1.22474487, 0, 1.22474487], "col2": [0, 0, 0], "col3": [1.22474487, 0, -1.22474487]}
    )
    result = task_func(dataframe)
    assert result.equals(expected_result)

    # Test case 2: Test with a dataframe with non-numeric columns
    data = {"col1": [1, 2, 3], "col2": ["a", "b", "c"], "col3": [7, 8, 9]}
    dataframe = pd.DataFrame(data)
    expected_result = pd.DataFrame(
        {"col1": [-1.22474487, 0, 1.22474487], "col2": [0, 0, 0], "col3": [1.22474487, 0, -1.22474487]}
    )
    result = task_func(dataframe)
    assert result.equals(expected_result)

    # Test case 3: Test with a dataframe with all non-numeric columns
    data = {"col1": ["a", "b", "c"], "col2": ["d", "e", "f"], "col3": ["g", "h", "i"]}
    dataframe = pd.DataFrame(data)
    expected_result = pd.DataFrame(
        {"col1": [0, 0, 0], "col2": [0, 0, 0], "col3": [0, 0, 0]}
    )
    result = task_func(dataframe)
    assert result.equals(expected_result)