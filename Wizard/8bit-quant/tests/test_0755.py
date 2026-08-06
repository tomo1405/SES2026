python
import numpy as np
import pandas as pd
from datetime import datetime
from src_0755 import task_func

# Constants
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def test_task_func_empty_array():
    result = []
    summary_series = task_func(result)
    assert summary_series['mean'].isnull()
    assert summary_series['median'].isnull()
    assert summary_series['min'].isnull()
    assert summary_series['max'].isnull()
    assert summary_series['std'].isnull()
    assert summary_series['current_time'] == datetime.now().strftime(DATE_FORMAT)

def test_task_func_non_numeric_values():
    result = [{'from_user': 'a'}, {'from_user': 'b'}]
    try:
        task_func(result)
        assert False, "Expected ValueError"
    except ValueError:
        assert True

def test_task_func_numeric_values():
    result = [{'from_user': 1}, {'from_user': 2}, {'from_user': 3}]
    summary_series = task_func(result)
    assert summary_series['mean'] == 2
    assert summary_series['median'] == 2
    assert summary_series['min'] == 1
    assert summary_series['max'] == 3
    assert summary_series['std'] == 1
    assert summary_series['current_time'] == datetime.now().strftime(DATE_FORMAT)