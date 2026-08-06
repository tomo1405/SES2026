import pandas as pd
import pytest
from src_0789 import task_func


def test_task_func():
    # Test case 1: N > 1
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10]})
    col1 = 'A'
    col2 = 'B'
    N = 3
    p_value = task_func(df, col1, col2, N)
    assert p_value > 0.05

    # Test case 2: N <= 1
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10]})
    col1 = 'A'
    col2 = 'B'
    N = 1
    with pytest.raises(ValueError):
        task_func(df, col1, col2, N)

    # Test case 3: Columns not found in the DataFrame
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10]})
    col1 = 'C'
    col2 = 'D'
    N = 3
    with pytest.raises(ValueError):
        task_func(df, col1, col2, N)

    # Test case 4: Valid input
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10]})
    col1 = 'A'
    col2 = 'B'
    N = 3
    p_value = task_func(df, col1, col2, N)
    assert p_value > 0.05