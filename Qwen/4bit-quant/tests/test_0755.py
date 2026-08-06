import pytest
from src_0755 import task_func
import numpy as np
import pandas as pd
from datetime import datetime

def test_task_func_empty_input():
    result = []
    summary_series = task_func(result)
    assert summary_series['mean'] == np.nan
    assert summary_series['median'] == np.nan
    assert summary_series['min'] == np.nan
    assert summary_series['max'] == np.nan
    assert summary_series['std'] == np.nan
    assert isinstance(summary_series['current_time'], str)

def test_task_func_non_numeric_values():
    result = [{'from_user': 'a'}, {'from_user': 'b'}]
    with pytest.raises(ValueError, match="from_user values should be numeric only."):
        task_func(result)

def test_task_func_numeric_values():
    result = [{'from_user': 1}, {'from_user': 2}, {'from_user': 3}]
    summary_series = task_func(result)
    assert summary_series['mean'] == 2.0
    assert summary_series['median'] == 2.0
    assert summary_series['min'] == 1.0
    assert summary_series['max'] == 3.0
    assert np.isclose(summary_series['std'], np.std([1, 2, 3]))
    assert isinstance(summary_series['current_time'], str)

def test_task_func_single_value():
    result = [{'from_user': 5}]
    summary_series = task_func(result)
    assert summary_series['mean'] == 5.0
    assert summary_series['median'] == 5.0
    assert summary_series['min'] == 5.0
    assert summary_series['max'] == 5.0
    assert summary_series['std'] == 0.0
    assert isinstance(summary_series['current_time'], str)

def test_task_func_with_none_values():
    result = [{'from_user': None}, {'from_user': 2}, {'from_user': 3}]
    with pytest.raises(ValueError, match="from_user values should be numeric only."):
        task_func(result)