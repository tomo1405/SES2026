import numpy as np
import matplotlib.pyplot as plt
from src_0971 import task_func

def test_task_func_valid_input():
    data = np.array([1, 2, 3, 4, 5])
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)

def test_task_func_negative_numbers():
    data = np.array([1, 2, 3, 4, 5, -1])
    try:
        task_func(data)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError not raised"

def test_task_func_nans():
    data = np.array([1, 2, np.nan, 4, 5])
    try:
        task_func(data)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError not raised"

def test_task_func_non_numeric():
    data = np.array(["a", "b", "c", "d", "e"])
    try:
        task_func(data)
    except TypeError:
        pass
    else:
        assert False, "Expected TypeError not raised"