import pytest
from src_0421 import task_func
import pandas as pd
from sklearn.preprocessing import StandardScaler


def test_task_func():
    # Test case 1: Test that the function returns a DataFrame
    data = [[1, 2], [3, 4]]
    result = task_func(data)
    assert isinstance(result, pd.DataFrame)

    # Test case 2: Test that the function scales numeric columns
    data = [[1, 2], [3, 4]]
    result = task_func(data)
    assert result.equals(pd.DataFrame([[0, 0], [0, 0]], columns=["a", "b"]))

    # Test case 3: Test that the function does not scale non-numeric columns
    data = [["a", "b"], ["c", "d"]]
    result = task_func(data)
    assert result.equals(pd.DataFrame([["a", "b"], ["c", "d"]], columns=["a", "b"]))

    # Test case 4: Test that the function handles missing values
    data = [[1, 2], [3, 4], [5, None]]
    result = task_func(data)
    assert result.equals(pd.DataFrame([[0, 0], [0, 0], [0, None]], columns=["a", "b"]))

    # Test case 5: Test that the function handles non-numeric values
    data = [[1, 2], [3, 4], ["a", "b"]]
    result = task_func(data)
    assert result.equals(pd.DataFrame([[0, 0], [0, 0], ["a", "b"]], columns=["a", "b"]))