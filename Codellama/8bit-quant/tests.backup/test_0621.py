import pytest
from src_0621 import task_func
import numpy as np
import pandas as pd

def test_task_func():
    L = [(1, 2), (3, 4)]
    df = task_func(L)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (1 * 2, 3 * 4)
    assert np.all(df.values >= RANGE[0])
    assert np.all(df.values <= RANGE[1])