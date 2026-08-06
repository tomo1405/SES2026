import pandas as pd
import matplotlib.pyplot as plt
import pytest
from src_0905 import task_func

@pytest.fixture
def input_data():
    return [
        {'x': 1, 'y': 2, 'z': 3},
        {'x': 4, 'y': 5, 'z': 6},
        {'x': 7, 'y': 8, 'z': 9},
    ]

def test_task_func(input_data):
    ax = task_func(input_data)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_keys(input_data):
    ax = task_func(input_data, keys=['x', 'y'])
    assert isinstance(ax, plt.Axes)

def test_task_func_with_invalid_keys(input_data):
    with pytest.raises(ValueError):
        task_func(input_data, keys=['a', 'b'])