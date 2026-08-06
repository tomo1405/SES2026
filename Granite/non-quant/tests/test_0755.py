from datetime import datetime

import numpy as np
import pandas as pd
import pytest
from src_0755 import task_func


def test_task_func_with_numeric_input():
    result = [{'from_user': 1}, {'from_user': 2}, {'from_user': 3}]
    expected_output = pd.Series({
        'mean': 2,
        'median': 2,
        'min': 1,
        'max': 3,
        'std': 1,
        'current_time': datetime.now().strftime(DATE_FORMAT)
    })
    actual_output = task_func(result)
    assert actual_output.equals(expected_output)

def test_task_func_with_empty_input():
    result = []
    expected_output = pd.Series({
        'mean': np.nan,
        'median': np.nan,
        'min': np.nan,
        'max': np.nan,
        'std': np.nan,
        'current_time': datetime.now().strftime(DATE_FORMAT)
    })
    actual_output = task_func(result)
    assert actual_output.equals(expected_output)

def test_task_func_with_non_numeric_input():
    result = [{'from_user': 'a'}, {'from_user': 'b'}, {'from_user': 'c'}]
    with pytest.raises(ValueError) as excinfo:
        task_func(result)
    assert "from_user values should be numeric only." in str(excinfo.value)