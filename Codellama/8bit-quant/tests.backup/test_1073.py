import pytest
from src_1073 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    series_list = task_func(list_of_lists)
    assert len(series_list) == 3
    assert all(isinstance(s, pd.Series) for s in series_list)
    assert all(s.index.isin(list_of_lists[i]) for i, s in enumerate(series_list))
    assert all(s.values.isin(np.arange(1, len(list_of_lists[i]) + 1)) for i, s in enumerate(series_list))
    assert all(s.values.isin(np.random.shuffle(np.arange(1, len(list_of_lists[i]) + 1))) for i, s in enumerate(series_list))