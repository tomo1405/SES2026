import pytest
from src_0458 import task_func
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    return [[1, 2, 3], [4, 5], [], [6, 7, 8, 9]]

def test_task_func_valid_input(sample_data):
    ax = task_func(sample_data)
    assert isinstance(ax, plt.Axes)

def test_task_func_empty_input():
    with pytest.raises(TypeError):
        task_func([])

def test_task_func_non_integer_input():
    with pytest.raises(TypeError):
        task_func([[1, 2, 'a'], [4, 5]])

def test_task_func_single_element():
    ax = task_func([[1]])
    assert isinstance(ax, plt.Axes)

def test_task_func_all_zeros():
    ax = task_func([[0, 0, 0], [0]])
    assert isinstance(ax, plt.Axes)

def test_task_func_large_numbers():
    ax = task_func([[1000000, 2000000], [3000000, 4000000]])
    assert isinstance(ax, plt.Axes)