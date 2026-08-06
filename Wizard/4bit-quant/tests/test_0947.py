python
import numpy as np
import pandas as pd
import random
import pytest

def task_func(rows=3, cols=2, min_val=0, max_val=100, seed=0):
    random.seed(seed)
    if min_val == max_val:
        matrix = np.full((rows, cols), min_val)
    else:
        matrix = np.array([[random.randrange(min_val, max_val) for j in range(cols)] for i in range(rows)])
    df = pd.DataFrame(matrix)
    return df

def test_task_func():
    # Test case 1: Default values
    df = task_func()
    assert df.shape == (3, 2)
    assert df.min().min() >= 0 and df.max().max() <= 100
    
    # Test case 2: Custom values
    df = task_func(rows=5, cols=3, min_val=10, max_val=20, seed=1)
    assert df.shape == (5, 3)
    assert df.min().min() >= 10 and df.max().max() <= 20
    
    # Test case 3: Min and max values are equal
    df = task_func(rows=2, cols=3, min_val=100, max_val=100, seed=2)
    assert df.shape == (2, 3)
    assert df.min().min() == 100 and df.max().max() == 100
    
    # Test case 4: Rows and cols are equal
    df = task_func(rows=5, cols=5, min_val=0, max_val=100, seed=3)
    assert df.shape == (5, 5)
    assert df.min().min() >= 0 and df.max().max() <= 100
    
    # Test case 5: Negative values
    with pytest.raises(ValueError):
        df = task_func(rows=2, cols=3, min_val=-10, max_val=20, seed=4)
    
    # Test case 6: Max value is less than min value
    with pytest.raises(ValueError):
        df = task_func(rows=2, cols=3, min_val=20, max_val=10, seed=5)