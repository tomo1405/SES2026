import pytest
from src_0458 import task_func
import pandas as pd
import numpy as np

def test_task_func_valid_input():
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ax = task_func(L)
    assert isinstance(ax, pd.Series)
    assert ax.dtype == np.int64
    assert ax.plot.kind == "hist"
    assert ax.plot.rwidth == 0.8
    assert ax.plot.bins == len(np.unique(np.concatenate([l for l in L if l])))

def test_task_func_invalid_input():
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1.1, 2.2, 3.3]]
    with pytest.raises(TypeError):
        task_func(L)