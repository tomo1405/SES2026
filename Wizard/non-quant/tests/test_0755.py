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

# Test the function
def test_task_func():
    # Test case 1
    result = [{'from_user': 1}, {'from_user': 2}, {'from_user': 3}]
    expected_summary = pd.Series({'mean': 2.0, 'median': 2.0, 'min': 1, 'max': 3, 'std': 1.0, 'current_time': datetime.now().strftime(DATE_FORMAT)})
    assert task_func(result).equals(expected_summary)

    # Test case 2
    result = [{'from_user': 1}, {'from_user': 2}, {'from_user': 3}, {'from_user': np.nan}]
    expected_summary = pd.Series({'mean': 2.0, 'median': 2.0, 'min': 1, 'max': 3, 'std': 0.816496580927726, 'current_time': datetime.now().strftime(DATE_FORMAT)})
    assert task_func(result).equals(expected_summary)

    # Test case 3
    result = []
    expected_summary = pd.Series({'mean': np.nan, 'median': np.nan, 'min': np.nan, 'max': np.nan, 'std': np.nan, 'current_time': datetime.now().strftime(DATE_FORMAT)})
    assert task_func(result).equals(expected_summary)

    # Test case 4
    result = [{'from_user': 'a'}, {'from_user': 'b'}, {'from_user': 'c'}]
    try:
        task_func(result)
        assert False
    except ValueError as e:
        assert str(e) == "from_user values should be numeric only."

    # Test case 5
    result = [{'from_user': 1}, {'from_user': 2}, {'from_user': 'c'}]
    try:
        task_func(result)
        assert False
    except ValueError as e:
        assert str(e) == "from_user values should be numeric only."

test_task_func()