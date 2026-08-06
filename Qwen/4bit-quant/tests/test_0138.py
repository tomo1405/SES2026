import pytest
from src_0138 import task_func
import pandas as pd
from scipy.stats import skew

def test_task_func_input_type():
    with pytest.raises(ValueError):
        task_func([])

def test_task_func_empty_dataframe():
    with pytest.raises(ValueError):
        task_func(pd.DataFrame())

def test_task_func_skewness_calculation():
    data = {'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1]}
    df = pd.DataFrame(data)
    expected_skewness = skew(df['B'].dropna())
    assert task_func(df) == expected_skewness

def test_task_func_with_nan_values():
    data = {'A': [1, 2, None, 4, 5], 'B': [5, None, 3, 2, 1]}
    df = pd.DataFrame(data)
    expected_skewness = skew(df['B'].dropna())
    assert task_func(df) == expected_skewness

def test_task_func_single_column():
    data = {'A': [1, 2, 3, 4, 5]}
    df = pd.DataFrame(data)
    expected_skewness = skew(df['A'].dropna())
    assert task_func(df) == expected_skewness