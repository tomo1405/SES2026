python
import pandas as pd
import numpy as np
import pytest

def task_func(d):
    if not isinstance(d, list) or any(not isinstance(item, dict) for item in d):
        raise ValueError("Input must be a list of dictionaries.")
    
    if not d:
        return {key: None for key in ['x', 'y', 'z']}

    df = pd.DataFrame(d).fillna(0)  # Replace missing values with 0 to allow computations
    stats = {}

    for key in ['x', 'y', 'z']:
        if key in df.columns:
            stats[key] = {
                'mean': np.mean(df[key]),
                'sum': np.sum(df[key]),
                'max': np.max(df[key]),
                'min': np.min(df[key]),
                'std': np.std(df[key], ddof=0)  # Population standard deviation
            }
        else:
            stats[key] = None

    return stats

def test_task_func():
    # Test case 1: Empty list
    assert task_func([]) == {'x': None, 'y': None, 'z': None}

    # Test case 2: List with missing values
    data = [
        {'x': 1, 'y': 2, 'z': 3},
        {'x': 4, 'y': 5, 'z': 6},
        {'x': None, 'y': 7, 'z': 8},
        {'x': 9, 'y': None, 'z': 10},
        {'x': 11, 'y': 12, 'z': None}
    ]
    expected_stats = {
        'x': {'mean': 6.0, 'sum': 30, 'max': 11, 'min': 1, 'std': 4.242640687119285},
        'y': {'mean': 8.0, 'sum': 40, 'max': 12, 'min': 2, 'std': 2.8284271247461903},
        'z': {'mean': 9.0, 'sum': 30, 'max': 10, 'min': 3, 'std': 3.3166247903554},
    }
    assert task_func(data) == expected_stats

    # Test case 3: List with invalid data type
    with pytest.raises(ValueError):
        task_func('not a list')

    # Test case 4: List with invalid data type
    with pytest.raises(ValueError):
        task_func([{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'y': 5, 'z': 6}, 'not a dict'])