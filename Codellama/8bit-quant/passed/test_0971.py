import pytest
from src_0971 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_valid_input():
    data = np.array([1, 2, 3, 4, 5])
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == "Index"
    assert ax.get_ylabel() == "Cumulative Probability"
    assert ax.get_title() == "Cumulative Probability Plot"

def test_task_func_invalid_input():
    data = np.array([-1, 2, 3, 4, 5])
    with pytest.raises(ValueError):
        task_func(data)

    data = np.array([1, 2, 3, 4, np.nan])
    with pytest.raises(ValueError):
        task_func(data)

    data = np.array([1, 2, 3, 4, "a"])
    with pytest.raises(TypeError):
        task_func(data)