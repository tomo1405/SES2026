import pytest
import numpy as np
import pandas as pd
import statistics

def task_func(rows, columns=['A', 'B', 'C', 'D', 'E', 'F'], seed=42):
    if not isinstance(rows, int) or rows <= 0:
        raise ValueError("rows must be a positive integer greater than 0.")

    np.random.seed(seed)
    data = np.random.randint(1, 101, size=(rows, len(columns)))
    df = pd.DataFrame(data, columns=columns)
    
    stats_dict = {}
    for col in columns:
        stats_dict[col] = {
            'mean': statistics.mean(df[col]),
            'median': statistics.median(df[col])
        }
    
    return df, stats_dict

def test_task_func():
    # Test case 1: rows is a positive integer
    df, stats_dict = task_func(rows=5)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(stats_dict, dict)
    assert len(stats_dict) == 6
    for col in ['A', 'B', 'C', 'D', 'E', 'F']:
        assert col in stats_dict
        assert isinstance(stats_dict[col], dict)
        assert 'mean' in stats_dict[col]
        assert 'median' in stats_dict[col]
    # Test case 2: rows is not a positive integer
    with pytest.raises(ValueError):
        task_func(rows=-1)
    with pytest.raises(ValueError):
        task_func(rows='abc')
    with pytest.raises(ValueError):
        task_func(rows=0)