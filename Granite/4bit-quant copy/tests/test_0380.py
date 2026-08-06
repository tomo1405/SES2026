import pandas as pd
import numpy as np
from src_0380 import task_func
import pytest

# Constants
COLUMNS = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']

def test_task_func():
    # Test case 1: length = 10
    df = task_func(10)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (10, len(COLUMNS))
    assert df.columns.tolist() == COLUMNS

    # Test case 2: length = 5
    df = task_func(5)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (5, len(COLUMNS))
    assert df.columns.tolist() == COLUMNS

    # Test case 3: length = 0
    with pytest.raises(ValueError):
        task_func(0)

    # Test case 4: length = -1
    with pytest.raises(ValueError):
        task_func(-1)