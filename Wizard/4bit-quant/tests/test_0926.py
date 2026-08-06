python
import pandas as pd
import numpy as np
import pytest

def task_func(data_size=1000, column_names=['A', 'B', 'C', 'D', 'E'], seed=0):
    np.random.seed(seed)
    df = pd.DataFrame(np.random.randint(1, 101, size=(data_size, len(column_names))), columns=column_names)
    df[df < 10] = -1  # Correctly replace values less than 10 with -1
    return df

def test_task_func():
    # Test case 1: data_size=100, column_names=['A', 'B', 'C'], seed=0
    df = task_func(data_size=100, column_names=['A', 'B', 'C'], seed=0)
    assert df.shape == (100, 3)
    assert df.columns.tolist() == ['A', 'B', 'C']
    assert df.loc[0, 'A'] == 1
    assert df.loc[99, 'C'] == 99
    
    # Test case 2: data_size=1000, column_names=['A', 'B', 'C', 'D', 'E'], seed=0
    df = task_func(data_size=1000, column_names=['A', 'B', 'C', 'D', 'E'], seed=0)
    assert df.shape == (1000, 5)
    assert df.columns.tolist() == ['A', 'B', 'C', 'D', 'E']
    assert df.loc[0, 'A'] == 1
    assert df.loc[999, 'E'] == 999
    
    # Test case 3: data_size=1000, column_names=['A', 'B', 'C', 'D', 'E'], seed=1
    df = task_func(data_size=1000, column_names=['A', 'B', 'C', 'D', 'E'], seed=1)
    assert df.shape == (1000, 5)
    assert df.columns.tolist() == ['A', 'B', 'C', 'D', 'E']
    assert df.loc[0, 'A'] == 1
    assert df.loc[999, 'E'] == 999
    
    # Test case 4: data_size=1000, column_names=['A', 'B', 'C', 'D', 'E'], seed=100
    df = task_func(data_size=1000, column_names=['A', 'B', 'C', 'D', 'E'], seed=100)
    assert df.shape == (1000, 5)
    assert df.columns.tolist() == ['A', 'B', 'C', 'D', 'E']
    assert df.loc[0, 'A'] == 1
    assert df.loc[999, 'E'] == 999
    
    # Test case 5: data_size=1000, column_names=['A', 'B', 'C', 'D', 'E'], seed=1000
    df = task_func(data_size=1000, column_names=['A', 'B', 'C', 'D', 'E'], seed=1000)
    assert df.shape == (1000, 5)
    assert df.columns.tolist() == ['A', 'B', 'C', 'D', 'E']
    assert df.loc[0, 'A'] == 1
    assert df.loc[999, 'E'] == 999
    
    # Test case 6: data_size=1000, column_names=['A', 'B', 'C', 'D', 'E'], seed=10000
    df = task_func(data_size=1000, column_names=['A', 'B', 'C', 'D', 'E'], seed=10000)
    assert df.shape == (1000, 5)
    assert df.columns.tolist() == ['A', 'B', 'C', 'D', 'E']
    assert df.loc[0, 'A'] == 1
    assert df.loc[999, 'E'] == 999
    
    # Test case 7: data_size=1000, column_names=['A', 'B', 'C', 'D', 'E'], seed=100000
    df = task_func(data_size=1000, column_names=['A', 'B', 'C', 'D', 'E'], seed=100000)
    assert df.shape == (1000, 5)
    assert df.columns.tolist() == ['A', 'B', 'C', 'D', 'E']
    assert df.loc[0, 'A'] == 1
    assert df.loc[999, 'E'] == 999
    
    # Test case 8: data_size=1000, column_names=['A', 'B', 'C', 'D', 'E'], seed=1000000
    df = task_func(data_size=1000, column_names=['A', 'B', 'C', 'D', 'E'], seed=1000000)
    assert df.shape == (1000, 5)
    assert df.columns.tolist() == ['A', 'B', 'C', 'D', 'E']
    assert df.loc[0, 'A'] == 1
    assert df.loc[999, 'E'] == 999
    
    # Test case 9: data_size=1000, column_names=['A', 'B', 'C', 'D', 'E'], seed=10000000
    df = task_func(data_size=1000, column_names=['A', 'B', 'C', 'D', 'E'], seed=10000000)
    assert df.shape == (1000, 5)
    assert df.columns.tolist() == ['A', 'B', 'C', 'D', 'E']
    assert df.loc[0, 'A'] == 1
    assert df.loc[999, 'E'] == 999
    
    # Test case 10: data_size=1000, column_names=['A', 'B', 'C', 'D', 'E'], seed=100000000
    df = task_func(data_size=1000, column_names=['A', 'B', 'C', 'D', 'E'], seed=100000000)
    assert df.shape == (1000, 5)
    assert df.columns.tolist() == ['A', 'B', 'C', 'D', 'E']
    assert df.loc[0, 'A'] == 1
    assert df.loc[999, 'E'] == 999