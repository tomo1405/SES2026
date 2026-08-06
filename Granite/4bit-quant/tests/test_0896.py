import matplotlib.pyplot as plt
import numpy as np
from src_0896 import task_func


def test_task_func():
    array, mean, std, ax = task_func()
    assert isinstance(array, np.ndarray)
    assert isinstance(mean, float)
    assert isinstance(std, float)
    assert isinstance(ax, plt.Axes)