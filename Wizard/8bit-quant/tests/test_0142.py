python
import numpy as np
import pandas as pd
import statistics
import pytest

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
    # Test case 1: Valid input
    df, stats_dict = task_func(10)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(stats_dict, dict)
    assert len(df) == 10
    assert len(stats_dict) == 6
    assert all(col in df.columns for col in ['A', 'B', 'C', 'D', 'E', 'F'])
    assert all(col in stats_dict for col in ['A', 'B', 'C', 'D', 'E', 'F'])
    assert all(isinstance(stats_dict[col]['mean'], float) for col in stats_dict)
    assert all(isinstance(stats_dict[col]['median'], float) for col in stats_dict)
    
    # Test case 2: Invalid input (rows <= 0)
    with pytest.raises(ValueError):
        task_func(0)
    
    # Test case 3: Invalid input (rows not an integer)
    with pytest.raises(ValueError):
        task_func('a')