python
import numpy as np
import pandas as pd
import pytest

def task_func(rows, columns, seed=None):
    if seed is not None:
        np.random.seed(seed)
    matrix = np.random.rand(rows, columns)
    df = pd.DataFrame(matrix)
    
    return df

def test_task_func():
    # Test case 1
    df = task_func(3, 4)
    assert df.shape == (3, 4)
    assert df.iloc[0, 0] >= 0 and df.iloc[0, 0] < 1
    
    # Test case 2
    df = task_func(5, 2, 123)
    assert df.shape == (5, 2)
    assert df.iloc[0, 0] == 0.5488135039273248
    assert df.iloc[1, 1] == 0.9002158953651292
    
    # Test case 3
    with pytest.raises(ValueError):
        task_func(0, 2)
        
    # Test case 4
    with pytest.raises(ValueError):
        task_func(2, 0)