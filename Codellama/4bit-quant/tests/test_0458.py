import pytest
from src_0458 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ax = task_func(L)
    assert isinstance(ax, pd.Series)
    assert ax.dtype == np.dtype("int")
    assert len(ax.unique()) == 3
    assert ax.plot(kind="hist", rwidth=0.8, bins=3)

def test_task_func_invalid_input():
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    with pytest.raises(TypeError):
        task_func(L, dtype=np.float64)