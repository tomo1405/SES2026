import pandas as pd
import numpy as np
import pytest
from src_1030 import task_func

def test_task_func():
    # Test with default arguments
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (100, 3)
    assert all(df.columns == ['a', 'b', 'c'])

    # Test with custom arguments
    df = task_func(rows=50, columns=5)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (50, 5)
    assert all(df.columns == ['a', 'b', 'c', 'd', 'e'])

    # Test with invalid arguments
    with pytest.raises(ValueError):
        df = task_func(rows=-1)
    with pytest.raises(ValueError):
        df = task_func(columns=-1)