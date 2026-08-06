import pytest
import numpy as np
import pandas as pd
from datetime import datetime
from src_0755 import task_func

def test_task_func_with_numeric_values():
    result = [{'from_user': 1}, {'from_user': 2}, {'from_user': 3}]
    expected_summary = pd.Series({
        'mean': 2,
        'median': 2,
        'min': 1,
        'max': 3,
        'std': 1,
        'current_time': datetime.now().strftime(DATE_FORMAT)
    })
    summary_series = task_func(result)
    assert summary_series.equals(expected_summary)

def test_task_func_with_non_numeric_values():
    result = [{'from_user': 1}, {'from_user': 2}, {'from_user': 'a'}]
    with pytest.raises(ValueError) as excinfo:
        task_func(result)
    assert "from_user values should be numeric only." in str(excinfo.value)

def test_task_func_with_empty_array():
    result = []
    expected_summary = pd.Series({
        'mean': np.nan,
        'median': np.nan,
        'min': np.nan,
        'max': np.nan,
        'std': np.nan,
        'current_time': datetime.now().strftime(DATE_FORMAT)
    })
    summary_series = task_func(result)
    assert summary_series.equals(expected_summary)