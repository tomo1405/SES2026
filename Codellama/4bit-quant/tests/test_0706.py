import pandas as pd
import pytest
from src_0706 import task_func


def test_task_func():
    # Test case 1: column exists in DataFrame
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    column = 'A'
    alpha = 0.05
    assert task_func(df, column, alpha) == True

    # Test case 2: column does not exist in DataFrame
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    column = 'C'
    alpha = 0.05
    with pytest.raises(ValueError):
        task_func(df, column, alpha)

    # Test case 3: column exists in DataFrame, but alpha is not a float
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    column = 'A'
    alpha = '0.05'
    with pytest.raises(TypeError):
        task_func(df, column, alpha)

    # Test case 4: column exists in DataFrame, but alpha is not a valid float
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    column = 'A'
    alpha = 1.1
    with pytest.raises(ValueError):
        task_func(df, column, alpha)

    # Test case 5: column exists in DataFrame, but alpha is not a valid float
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    column = 'A'
    alpha = -0.05
    with pytest.raises(ValueError):
        task_func(df, column, alpha)