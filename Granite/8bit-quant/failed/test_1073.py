import pandas as pd
import numpy as np
import pytest
from src_1073 import task_func

def test_task_func():
    list_of_lists = [['a', 'b', 'c'], ['d', 'e', 'f']]
    series_list = task_func(list_of_lists)
    for series in series_list:
        assert isinstance(series, pd.Series)
        assert len(series) == len(list_of_lists[0])
        assert all(series.index == list_of_lists[0])