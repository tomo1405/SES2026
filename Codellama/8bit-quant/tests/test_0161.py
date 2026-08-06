import pytest
from src_0161 import task_func
import pandas as pd
import seaborn as sns
from scipy import stats


def test_task_func_valid_input():
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12], 'E': [13, 14, 15], 'F': [16, 17, 18], 'G': [19, 20, 21], 'H': [22, 23, 24]})
    df, ax, p = task_func(data)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, sns.axis.Axis)
    assert isinstance(p, float)


def test_task_func_invalid_input():
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12], 'E': [13, 14, 15], 'F': [16, 17, 18], 'G': [19, 20, 21]})
    with pytest.raises(ValueError):
        task_func(data)


def test_task_func_normaltest():
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12], 'E': [13, 14, 15], 'F': [16, 17, 18], 'G': [19, 20, 21], 'H': [22, 23, 24]})
    df, ax, p = task_func(data)
    assert p is not None


def test_task_func_normaltest_not_enough_samples():
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12], 'E': [13, 14, 15], 'F': [16, 17, 18], 'G': [19, 20, 21], 'H': [22, 23, 24]})
    df, ax, p = task_func(data)
    assert p is None