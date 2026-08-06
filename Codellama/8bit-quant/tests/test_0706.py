import pandas as pd
from src_0706 import task_func


def test_task_func():
    # Test case 1: column exists in DataFrame
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    column = 'A'
    alpha = 0.05
    expected_result = True
    actual_result = task_func(df, column, alpha)
    assert actual_result == expected_result

    # Test case 2: column does not exist in DataFrame
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    column = 'C'
    alpha = 0.05
    expected_result = False
    actual_result = task_func(df, column, alpha)
    assert actual_result == expected_result

    # Test case 3: column exists in DataFrame, but alpha is too high
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    column = 'A'
    alpha = 0.99
    expected_result = False
    actual_result = task_func(df, column, alpha)
    assert actual_result == expected_result

    # Test case 4: column exists in DataFrame, but alpha is too low
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    column = 'A'
    alpha = 0.001
    expected_result = True
    actual_result = task_func(df, column, alpha)
    assert actual_result == expected_result