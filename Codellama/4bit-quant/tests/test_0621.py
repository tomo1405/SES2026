import pytest
from src_0621 import task_func
import numpy as np
import pandas as pd

def test_task_func():
    L = [(10, 5), (20, 10)]
    df = task_func(L)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (100, 100)
    assert np.all(df.values >= RANGE[0])
    assert np.all(df.values <= RANGE[1])