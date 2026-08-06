import pytest
from src_1073 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    series_list = task_func(list_of_lists)
    assert len(series_list) == 3
    assert all(isinstance(s, pd.Series) for s in series_list)
    assert all(s.index.equals(sublist) for sublist, s in zip(list_of_lists, series_list))
    assert all(np.allclose(s.values, np.arange(1, len(sublist) + 1)) for sublist, s in zip(list_of_lists, series_list))

def test_task_func_empty_list():
    list_of_lists = []
    series_list = task_func(list_of_lists)
    assert len(series_list) == 0

def test_task_func_single_element_list():
    list_of_lists = [[1]]
    series_list = task_func(list_of_lists)
    assert len(series_list) == 1
    assert isinstance(series_list[0], pd.Series)
    assert series_list[0].index.equals([1])
    assert np.allclose(series_list[0].values, np.arange(1, 2))

def test_task_func_duplicate_elements():
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    series_list = task_func(list_of_lists)
    assert len(series_list) == 3
    assert all(isinstance(s, pd.Series) for s in series_list)
    assert all(s.index.equals(sublist) for sublist, s in zip(list_of_lists, series_list))
    assert all(np.allclose(s.values, np.arange(1, len(sublist) + 1)) for sublist, s in zip(list_of_lists, series_list))

def test_task_func_non_list_input():
    with pytest.raises(TypeError):
        task_func(1)

def test_task_func_non_list_of_lists_input():
    with pytest.raises(TypeError):
        task_func([1, 2, 3])

def test_task_func_non_list_of_lists_of_lists_input():
    with pytest.raises(TypeError):
        task_func([[1, 2, 3], [4, 5, 6], [7, 8, 9], 10])