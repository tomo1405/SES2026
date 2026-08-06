python
import pandas as pd
import numpy as np
import pytest

# Constants
COLUMNS = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']

def task_func(length):

    data = np.random.randint(0,100,size=(length, len(COLUMNS)))
    df = pd.DataFrame(data, columns=COLUMNS)

    return df

def test_task_func():
    # Test case 1
    df = task_func(10)
    assert df.shape == (10, 5)
    assert df.columns.tolist() == COLUMNS
    assert df.dtypes.tolist() == [np.dtype('int64')] * 5

    # Test case 2
    df = task_func(0)
    assert df.shape == (0, 5)
    assert df.columns.tolist() == COLUMNS
    assert df.dtypes.tolist() == [np.dtype('int64')] * 5

    # Test case 3
    df = task_func(100)
    assert df.shape == (100, 5)
    assert df.columns.tolist() == COLUMNS
    assert df.dtypes.tolist() == [np.dtype('int64')] * 5