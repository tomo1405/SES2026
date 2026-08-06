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
    assert df.A.isin([-1]).sum() == 0
    assert df.B.isin([-1]).sum() == 0
    assert df.C.isin([-1]).sum() == 0

    # Test case 2: data_size=1000, column_names=['A', 'B', 'C', 'D', 'E'], seed=0
    df = task_func(data_size=1000, column_names=['A', 'B', 'C', 'D', 'E'], seed=0)
    assert df.shape == (1000, 5)
    assert df.A.isin([-1]).sum() == 0
    assert df.B.isin([-1]).sum() == 0
    assert df.C.isin([-1]).sum() == 0
    assert df.D.isin([-1]).sum() == 0
    assert df.E.isin([-1]).sum() == 0

    # Test case 3: data_size=1000, column_names=['A', 'B', 'C', 'D', 'E'], seed=1
    df = task_func(data_size=1000, column_names=['A', 'B', 'C', 'D', 'E'], seed=1)
    assert df.shape == (1000, 5)
    assert df.A.isin([-1]).sum() == 0
    assert df.B.isin([-1]).sum() == 0
    assert df.C.isin([-1]).sum() == 0
    assert df.D.isin([-1]).sum() == 0
    assert df.E.isin([-1]).sum() == 0