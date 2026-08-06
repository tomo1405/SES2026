import pytest
from src_0755 import task_func
import numpy as np
import pandas as pd
from datetime import datetime

def test_task_func_empty_input():
    result = []
    expected_summary = {
        'mean': np.nan,
        'median': np.nan,
        'min': np.nan,
        'max': np.nan,
        'std': np.nan,
        'current_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    assert task_func(result) == pd.Series(expected_summary)

def test_task_func_non_numeric_values():
    result = [{'from_user': 'a'}, {'from_user': 1}, {'from_user': 2}]
    with pytest.raises(ValueError):
        task_func(result)

def test_task_func_numeric_values():
    result = [{'from_user': 1}, {'from_user': 2}, {'from_user': 3}]
    expected_summary = {
        'mean': 2.0,
        'median': 2.0,
        'min': 1,
        'max': 3,
        'std': np.sqrt(((1-2)**2 + (2-2)**2 + (3-2)**2 / 3),
        'current_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    assert task_func(result) == pd.Series(expected_summary)