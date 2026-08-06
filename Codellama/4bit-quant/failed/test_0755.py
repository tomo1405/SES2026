import pytest
from src_0755 import task_func
import numpy as np
import pandas as pd
from datetime import datetime

def test_task_func():
    result = [{'from_user': 1}, {'from_user': 2}, {'from_user': 3}]
    summary = task_func(result)
    assert summary['mean'] == 2
    assert summary['median'] == 2
    assert summary['min'] == 1
    assert summary['max'] == 3
    assert summary['std'] == 1
    assert summary['current_time'] == datetime.now().strftime(DATE_FORMAT)

def test_task_func_empty_array():
    result = []
    summary = task_func(result)
    assert summary['mean'] == np.nan
    assert summary['median'] == np.nan
    assert summary['min'] == np.nan
    assert summary['max'] == np.nan
    assert summary['std'] == np.nan
    assert summary['current_time'] == datetime.now().strftime(DATE_FORMAT)

def test_task_func_non_numeric_values():
    result = [{'from_user': 'a'}, {'from_user': 'b'}, {'from_user': 'c'}]
    with pytest.raises(ValueError):
        task_func(result)