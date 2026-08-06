python
import numpy as np
import pandas as pd
import pytest
from scipy import stats

def task_func(df, column, alpha):
    # Artificial step to use np.mean for demonstration
    mean_value = np.mean(df[column])

    # Adjusting DataFrame for demonstration, this step is artificial
    df[column] = df[column] - mean_value

    if column not in df.columns:
        raise ValueError('Column does not exist in DataFrame')

    _, p = stats.shapiro(df[column])
    return p > alpha

def test_task_func():
    # Test case 1: valid input
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10]})
    column = 'A'
    alpha = 0.05
    expected_result = True
    result = task_func(df, column, alpha)
    assert result == expected_result

    # Test case 2: invalid input (column does not exist in DataFrame)
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10]})
    column = 'C'
    alpha = 0.05
    with pytest.raises(ValueError):
        task_func(df, column, alpha)

    # Test case 3: invalid input (alpha is not a float)
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10]})
    column = 'A'
    alpha = '0.05'
    with pytest.raises(TypeError):
        task_func(df, column, alpha)

    # Test case 4: invalid input (alpha is not in range [0, 1])
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10]})
    column = 'A'
    alpha = 1.5
    with pytest.raises(ValueError):
        task_func(df, column, alpha)

    # Test case 5: invalid input (column is not a string)
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10]})
    column = 1
    alpha = 0.05
    with pytest.raises(TypeError):
        task_func(df, column, alpha)

    # Test case 6: invalid input (DataFrame is empty)
    df = pd.DataFrame({'A': [], 'B': []})
    column = 'A'
    alpha = 0.05
    with pytest.raises(ValueError):
        task_func(df, column, alpha)