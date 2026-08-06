import pandas as pd
import numpy as np
import pytest

from src_0458 import task_func

def test_task_func():
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ax = task_func(L)
    assert isinstance(ax, pd.Series)
    assert ax.dtype == np.int64
    assert len(ax.unique()) == 9

def test_task_func_invalid_input():
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['a', 'b', 'c']]
    with pytest.raises(TypeError):
        task_func(L)