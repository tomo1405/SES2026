import pytest
from src_0249 import task_func
import numpy as np
import matplotlib.pyplot as plt
import itertools

def test_task_func_empty_data():
    with pytest.raises(ValueError):
        task_func([])

def test_task_func_single_column():
    data_list = [[1], [2], [3]]
    result = task_func(data_list)
    assert result is not None

def test_task_func_multiple_columns():
    data_list = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    result = task_func(data_list)
    assert result is not None

def test_task_func_empty_data():
    with pytest.raises(ValueError):
        task_func([])