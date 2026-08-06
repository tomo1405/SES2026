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
    assert df.A.min() >= 1
    assert df.A.max() <= 100
    assert df.B.min() >= 1
    assert df.B.max() <= 100
    assert df.C.min() >= 1
    assert df.C.max() <= 100
    assert df.D.isnull().all()
    assert df.E.isnull().all()
    assert df.A.eq(-1).sum() == 0
    assert df.B.eq(-1).sum() == 0
    assert df.C.eq(-1).sum() == 0

    # Test case 2: data_size=1000, column_names=['A', 'B', 'C', 'D', 'E'], seed=0
    df = task_func(data_size=1000, column_names=['A', 'B', 'C', 'D', 'E'], seed=0)
    assert df.shape == (1000, 5)
    assert df.A.min() >= 1
    assert df.A.max() <= 100
    assert df.B.min() >= 1
    assert df.B.max() <= 100
    assert df.C.min() >= 1
    assert df.C.max() <= 100
    assert df.D.min() >= 1
    assert df.D.max() <= 100
    assert df.E.min() >= 1
    assert df.E.max() <= 100
    assert df.A.eq(-1).sum() == 0
    assert df.B.eq(-1).sum() == 0
    assert df.C.eq(-1).sum() == 0
    assert df.D.eq(-1).sum() == 0
    assert df.E.eq(-1).sum() == 0