import pytest
from src_0249 import task_func
import numpy as np
import matplotlib.pyplot as plt
import itertools

def test_task_func():
    data_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ax = task_func(data_list)
    assert ax.get_xlabel() == 'Position'
    assert ax.get_ylabel() == 'Value'
    assert ax.get_title() == 'Plot of Data'
    assert len(ax.get_lines()) == 3
    assert ax.get_lines()[0].get_label() == 'Position 1'
    assert ax.get_lines()[1].get_label() == 'Position 2'
    assert ax.get_lines()[2].get_label() == 'Position 3'

def test_task_func_empty_data():
    data_list = []
    with pytest.raises(ValueError):
        task_func(data_list)

def test_task_func_invalid_data():
    data_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
    with pytest.raises(ValueError):
        task_func(data_list)