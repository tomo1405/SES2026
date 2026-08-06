import pytest
from src_0755 import task_func
import numpy as np
import pandas as pd
from datetime import datetime

def test_task_func_empty_input():
    result = []
    summary_series = task_func(result)
    expected_summary = {
        'mean': np.nan,
        'median': np.nan,
        'min': np.nan,
        'max': np.nan,
        'std': np.nan,
        'current_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    expected_series = pd.Series(expected_summary)
    assert summary_series.equals(expected_series)

def test_task_func_non_numeric_values():
    result = [{'from_user': 'a'}, {'from_user': 'b'}]
    with pytest.raises(ValueError, match="from_user values should be numeric only."):
        task_func(result)

def test_task_func_numeric_values():
    result = [{'from_user': 1}, {'from_user': 2}, {'from_user': 3}]
    summary_series = task_func(result)
    expected_summary = {
        'mean': 2.0,
        'median': 2.0,
        'min': 1,
        'max': 3,
        'std': 1.0,
        'current_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    expected_series = pd.Series(expected_summary)
    assert summary_series.equals(expected_series)

def test_task_func_mixed_values():
    result = [{'from_user': 1}, {'from_user': 'b'}, {'from_user': 3}]
    with pytest.raises(ValueError, match="from_user values should be numeric only."):
        task_func(result)