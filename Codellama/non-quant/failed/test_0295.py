import pytest
from src_0295 import task_func
import pandas as pd
from sklearn.preprocessing import StandardScaler

def test_task_func():
    # Test case 1: Test that the function returns a DataFrame
    df = pd.DataFrame({'id': [1, 2, 3], 'age': [20, 30, 40], 'income': [10000, 20000, 30000]})
    result = task_func(df)
    assert isinstance(result, pd.DataFrame)

    # Test case 2: Test that the function raises a ValueError when the input DataFrame is empty
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df)

    # Test case 3: Test that the function raises a ValueError when the input DataFrame does not have the required columns
    df = pd.DataFrame({'id': [1, 2, 3], 'age': [20, 30, 40]})
    with pytest.raises(ValueError):
        task_func(df)

    # Test case 4: Test that the function returns the expected result for a valid input DataFrame
    df = pd.DataFrame({'id': [1, 2, 3], 'age': [20, 30, 40], 'income': [10000, 20000, 30000]})
    expected_result = pd.DataFrame({'id': [1, 2, 3], 'age': [0.0, 1.0, 2.0], 'income': [0.0, 1.0, 2.0]})
    result = task_func(df)
    assert result.equals(expected_result)