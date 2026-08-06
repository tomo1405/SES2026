import pytest
from src_0622 import task_func
from itertools import chain
import numpy as np
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

@pytest.fixture
def input_data():
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    data = list(chain(*L))
    data = np.array(data).reshape(-1, 1)
    return data

def test_task_func(input_data):
    ax = task_func([input_data])
    assert ax is not None
    assert isinstance(ax, plt.Axes)

def test_task_func_with_different_input(input_data):
    ax = task_func([[1], [2], [3]])
    assert ax is not None
    assert isinstance(ax, plt.Axes)

def test_task_func_with_invalid_input():
    with pytest.raises(ValueError):
        task_func("invalid input")