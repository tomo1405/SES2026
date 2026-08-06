python
import numpy as np
import pandas as pd
import pytest

# Constants
RANGE = (1, 100)

def task_func(L):
    rows, columns = L[0][0] * L[0][1], L[1][0] * L[1][1]
    random_array = np.random.randint(RANGE[0], RANGE[1], size=(rows, columns))
    df = pd.DataFrame(random_array)
    
    return df

def test_task_func():
    # Test case 1
    L = [(2, 3), (4, 5)]
    expected_df = pd.DataFrame(np.random.randint(RANGE[0], RANGE[1], size=(6, 10)))
    assert task_func(L).equals(expected_df)
    
    # Test case 2
    L = [(1, 2), (3, 4)]
    expected_df = pd.DataFrame(np.random.randint(RANGE[0], RANGE[1], size=(6, 8)))
    assert task_func(L).equals(expected_df)
    
    # Test case 3
    L = [(0, 0), (0, 0)]
    expected_df = pd.DataFrame(np.random.randint(RANGE[0], RANGE[1], size=(0, 0)))
    assert task_func(L).equals(expected_df)