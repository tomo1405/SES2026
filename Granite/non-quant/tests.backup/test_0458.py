import pandas as pd
import numpy as np
from src_0458 import task_func
import pytest

def test_task_func():
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ax = task_func(L)
    assert isinstance(ax, pd.Series)
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 'a', 12]]
    with pytest.raises(TypeError):
        task_func(L)