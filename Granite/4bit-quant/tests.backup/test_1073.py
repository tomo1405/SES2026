import pandas as pd
import numpy as np
import pytest

from src_1073 import task_func

def test_task_func():
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    series_list = task_func(list_of_lists)

    for i, sublist in enumerate(list_of_lists):
        assert len(series_list[i]) == len(sublist)
        assert all(series_list[i].index == sublist)
        assert all(series_list[i].values == np.arange(1, len(sublist) + 1))

def test_task_func_with_empty_list():
    list_of_lists = [[]]
    series_list = task_func(list_of_lists)

    assert len(series_list) == 1
    assert len(series_list[0]) == 0

def test_task_func_with_non_list_input():
    with pytest.raises(TypeError):
        task_func(123)