python
import numpy as np
import matplotlib.pyplot as plt
import pytest

ARRAY_SIZE = 10000

def task_func():
    array = np.random.randint(1, 500, size=ARRAY_SIZE)
    mean = np.mean(array)
    std = np.std(array)

    fig, ax = plt.subplots()
    ax.hist(array, bins='auto')
    ax.set_title('Histogram of Random Values')
    ax.set_xlabel('Val')
    ax.set_ylabel('Freq')
    return array, mean, std, ax

def test_task_func():
    array, mean, std, ax = task_func()
    assert array.shape == (ARRAY_SIZE,)
    assert mean > 0
    assert std > 0
    assert isinstance(ax, plt.Axes)