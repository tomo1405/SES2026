import pytest
from src_0706 import task_func
import numpy as np
from scipy import stats

def test_task_func():
    # Test case 1: Test that the function returns True when the p-value is greater than the alpha value
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10]})
    column = 'A'
    alpha = 0.05
    expected_result = True
    actual_result = task_func(df, column, alpha)
    assert actual_result == expected_result

    # Test case 2: Test that the function returns False when the p-value is less than the alpha value
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10]})
    column = 'A'
    alpha = 0.05
    expected_result = False
    actual_result = task_func(df, column, alpha)
    assert actual_result == expected_result

    # Test case 3: Test that the function raises a ValueError when the column does not exist in the DataFrame
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10]})
    column = 'C'
    alpha = 0.05
    with pytest.raises(ValueError):
        task_func(df, column, alpha)