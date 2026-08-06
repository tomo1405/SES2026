import pandas as pd
import pytest
from src_0202 import task_func


def test_task_func():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10]})
    column = 'A'
    value = 3
    expected_greater_avg = [4, 5]
    expected_num_greater_value = 2
    expected_ax = [1, 2, 3, 4, 5]

    greater_avg, num_greater_value, ax = task_func(df, column, value)

    assert greater_avg == expected_greater_avg
    assert num_greater_value == expected_num_greater_value
    assert ax == expected_ax

def test_task_func_invalid_column():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10]})
    column = 'C'
    value = 3

    with pytest.raises(ValueError):
        task_func(df, column, value)

def test_task_func_invalid_value():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10]})
    column = 'A'
    value = 'hello'

    with pytest.raises(ValueError):
        task_func(df, column, value)