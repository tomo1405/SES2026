import pytest
from src_0947 import task_func
import numpy as np
import pandas as pd
import random

def test_task_func():
    # Test case 1: Default parameters
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 2)
    assert (df.values >= 0).all() and (df.values <= 100).all()

    # Test case 2: Custom parameters
    df = task_func(rows=5, cols=4, min_val=10, max_val=20, seed=1)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (5, 4)
    assert (df.values >= 10).all() and (df.values <= 20).all()

    # Test case 3: Special case
    df = task_func(rows=1, cols=1, min_val=10, max_val=10, seed=0)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (1, 1)
    assert df.values[0, 0] == 10