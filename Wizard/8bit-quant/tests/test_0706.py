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
    df = pd.DataFrame({'col1': [1, 2, 3, 4, 5], 'col2': [6, 7, 8, 9, 10]})
    column = 'col1'
    alpha = 0.05
    expected_output = True
    assert task_func(df, column, alpha) == expected_output

    # Test case 2: invalid column name
    df = pd.DataFrame({'col1': [1, 2, 3, 4, 5], 'col2': [6, 7, 8, 9, 10]})
    column = 'col3'
    alpha = 0.05
    with pytest.raises(ValueError):
        task_func(df, column, alpha)

    # Test case 3: invalid alpha value
    df = pd.DataFrame({'col1': [1, 2, 3, 4, 5], 'col2': [6, 7, 8, 9, 10]})
    column = 'col1'
    alpha = 0.01
    expected_output = False
    assert task_func(df, column, alpha) == expected_output