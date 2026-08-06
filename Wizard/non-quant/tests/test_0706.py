python
import numpy as np
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
    df = pd.DataFrame({'column': [1, 2, 3, 4, 5]})
    column = 'column'
    alpha = 0.05
    expected_result = True
    result = task_func(df, column, alpha)
    assert result == expected_result

    # Test case 2: invalid input (column does not exist in DataFrame)
    df = pd.DataFrame({'column': [1, 2, 3, 4, 5]})
    column = 'invalid_column'
    alpha = 0.05
    with pytest.raises(ValueError):
        task_func(df, column, alpha)

    # Test case 3: invalid input (alpha is not a float)
    df = pd.DataFrame({'column': [1, 2, 3, 4, 5]})
    column = 'column'
    alpha = 'not_a_float'
    with pytest.raises(TypeError):
        task_func(df, column, alpha)

    # Test case 4: invalid input (alpha is negative)
    df = pd.DataFrame({'column': [1, 2, 3, 4, 5]})
    column = 'column'
    alpha = -0.05
    with pytest.raises(ValueError):
        task_func(df, column, alpha)

    # Test case 5: invalid input (alpha is greater than 1)
    df = pd.DataFrame({'column': [1, 2, 3, 4, 5]})
    column = 'column'
    alpha = 1.05
    with pytest.raises(ValueError):
        task_func(df, column, alpha)