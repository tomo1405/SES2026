import pytest
from src_0175 import task_func
import pandas as pd
import numpy as np

def test_task_func_input_type():
    with pytest.raises(ValueError):
        task_func([1, 2, 3], 'new_column', 0, 10)

def test_task_func_column_added():
    df = pd.DataFrame({'A': [1, 2, 3]})
    result = task_func(df, 'new_column', 0, 10)
    assert 'new_column' in result.columns

def test_task_func_column_values():
    df = pd.DataFrame({'A': [1, 2, 3]})
    result = task_func(df, 'new_column', 0, 10)
    assert all(result['new_column'] >= 0) and all(result['new_column'] <= 10)

def test_task_func_randomness():
    df = pd.DataFrame({'A': [1, 2, 3]})
    result1 = task_func(df, 'new_column', 0, 10)
    result2 = task_func(df, 'new_column', 0, 10)
    assert not result1.equals(result2)

def test_task_func_no_data_change():
    df = pd.DataFrame({'A': [1, 2, 3]})
    result = task_func(df, 'new_column', 0, 10)
    assert result['A'].equals(df['A'])