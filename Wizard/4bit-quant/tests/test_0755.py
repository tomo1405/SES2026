python
import numpy as np
import pandas as pd
from datetime import datetime

# Constants
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def task_func(result):
    from_user_values = np.array([d['from_user'] for d in result if 'from_user' in d])
    # Handle edge case of empty array
    if len(from_user_values) == 0:
        summary = {
            'mean': np.nan,
            'median': np.nan,
            'min': np.nan,
            'max': np.nan,
            'std': np.nan,
            'current_time': datetime.now().strftime(DATE_FORMAT)
        }
    
    elif not np.issubdtype(from_user_values.dtype, np.number):
         raise ValueError("from_user values should be numeric only.")


    else:
        summary = {
            'mean': np.mean(from_user_values),
            'median': np.median(from_user_values),
            'min': np.min(from_user_values),
            'max': np.max(from_user_values),
            'std': np.std(from_user_values),
            'current_time': datetime.now().strftime(DATE_FORMAT)
        }

    summary_series = pd.Series(summary)
    return summary_series

def test_task_func():
    # Test case 1: empty array
    result = []
    summary_series = task_func(result)
    assert summary_series['mean'] == np.nan
    assert summary_series['median'] == np.nan
    assert summary_series['min'] == np.nan
    assert summary_series['max'] == np.nan
    assert summary_series['std'] == np.nan
    assert summary_series['current_time'] == datetime.now().strftime(DATE_FORMAT)

    # Test case 2: non-numeric array
    result = [{'from_user': 'a'}, {'from_user': 'b'}]
    try:
        summary_series = task_func(result)
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "from_user values should be numeric only."

    # Test case 3: numeric array
    result = [{'from_user': 1}, {'from_user': 2}, {'from_user': 3}]
    summary_series = task_func(result)
    assert summary_series['mean'] == 2
    assert summary_series['median'] == 2
    assert summary_series['min'] == 1
    assert summary_series['max'] == 3
    assert summary_series['std'] == 1.0
    assert summary_series['current_time'] == datetime.now().strftime(DATE_FORMAT)