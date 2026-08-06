python
import re
import pandas as pd
import pytest

def task_func(df: pd.DataFrame) -> int:

    if not isinstance(df, pd.DataFrame):
        raise TypeError("df should be a DataFrame.")

    # Constants
    BRACKETS_PATTERN = '[(){}[\]]'

    return df.applymap(
        lambda x: len(re.findall(BRACKETS_PATTERN, str(x)))
        ).sum().sum()

def test_task_func():
    # Test case 1
    df = pd.DataFrame({'A': ['{[()]}', '()', '[]', '{}'], 'B': ['{[()]}', '()', '[]', '{}']})
    assert task_func(df) == 8

    # Test case 2
    df = pd.DataFrame({'A': ['{[()]}', '()', '[]', '{}'], 'B': ['{[()]}', '()', '[]', '{}']})
    assert task_func(df) == 8

    # Test case 3
    df = pd.DataFrame({'A': ['{[()]}', '()', '[]', '{}'], 'B': ['{[()]}', '()', '[]', '{}']})
    assert task_func(df) == 8

    # Test case 4
    df = pd.DataFrame({'A': ['{[()]}', '()', '[]', '{}'], 'B': ['{[()]}', '()', '[]', '{}']})
    assert task_func(df) == 8

    # Test case 5
    df = pd.DataFrame({'A': ['{[()]}', '()', '[]', '{}'], 'B': ['{[()]}', '()', '[]', '{}']})
    assert task_func(df) == 8

    # Test case 6
    df = pd.DataFrame({'A': ['{[()]}', '()', '[]', '{}'], 'B': ['{[()]}', '()', '[]', '{}']})
    assert task_func(df) == 8

    # Test case 7
    df = pd.DataFrame({'A': ['{[()]}', '()', '[]', '{}'], 'B': ['{[()]}', '()', '[]', '{}']})
    assert task_func(df) == 8

    # Test case 8
    df = pd.DataFrame({'A': ['{[()]}', '()', '[]', '{}'], 'B': ['{[()]}', '()', '[]', '{}']})
    assert task_func(df) == 8

    # Test case 9
    df = pd.DataFrame({'A': ['{[()]}', '()', '[]', '{}'], 'B': ['{[()]}', '()', '[]', '{}']})
    assert task_func(df) == 8

    # Test case 10
    df = pd.DataFrame({'A': ['{[()]}', '()', '[]', '{}'], 'B': ['{[()]}', '()', '[]', '{}']})
    assert task_func(df) == 8