import pandas as pd
import numpy as np
import pytest
from src_0380 import task_func

# Constants
COLUMNS = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']

def test_task_func():
    # Test case 1: Test with length=10
    df = task_func(length=10)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (10, len(COLUMNS))
    assert all(df.columns == COLUMNS)
    assert np.all(df.values >= 0) and np.all(df.values < 100)

    # Test case 2: Test with length=5
    df = task_func(length=5)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (5, len(COLUMNS))
    assert all(df.columns == COLUMNS)
    assert np.all(df.values >= 0) and np.all(df.values < 100)

    # Test case 3: Test with invalid length (string)
    with pytest.raises(TypeError):
        task_func(length='invalid')

    # Test case 4: Test with invalid length (negative number)
    with pytest.raises(ValueError):
        task_func(length=-5)