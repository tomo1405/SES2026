import pandas as pd
from src_0926 import task_func


def test_task_func():
    # Test 1: Check if the function returns a pandas DataFrame
    result = task_func()
    assert isinstance(result, pd.DataFrame)

    # Test 2: Check if the function returns the correct number of rows and columns
    expected_rows = 1000
    expected_cols = 5
    assert result.shape == (expected_rows, expected_cols)

    # Test 3: Check if the function correctly replaces values less than 10 with -1
    expected_values = [-1, -1, -1, -1, -1]
    assert (result[result < 10] == expected_values).all()

    # Test 4: Check if the function correctly returns values greater than or equal to 10
    expected_values = [10, 11, 12, 13, 14]
    assert (result[result >= 10] == expected_values).all()