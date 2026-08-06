import matplotlib.pyplot as plt
import numpy as np
import pytest
from src_0655 import task_func


def test_task_func():
    array = np.array([[1, 2], [3, 4], [5, 6]])
    target_value = 2
    popt, ax = task_func(array, target_value)
    assert isinstance(popt, np.ndarray)
    assert isinstance(ax, plt.Axes)

def test_task_func_not_enough_points():
    array = np.array([[1, 2], [3, 4], [5, 6]])
    target_value = 7
    with pytest.raises(ValueError):
        task_func(array, target_value)