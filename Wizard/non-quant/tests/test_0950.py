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
    # Test case 1: Test with default arguments
    df = task_func(3, 4)
    assert df.shape == (3, 4)
    assert df.values.min() >= 0 and df.values.max() < 1
    
    # Test case 2: Test with seed argument
    df = task_func(3, 4, seed=42)
    assert df.shape == (3, 4)
    assert df.values.min() >= 0 and df.values.max() < 1
    assert df.values.sum() == 1.0
    
    # Test case 3: Test with invalid arguments
    with pytest.raises(ValueError):
        task_func(0, 4)
    with pytest.raises(ValueError):
        task_func(3, 0)