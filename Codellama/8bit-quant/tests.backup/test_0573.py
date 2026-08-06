import pytest
from src_0573 import task_func
import numpy as np

def test_task_func():
    array_length = 100
    array1 = np.array([randint(1, 100) for _ in range(array_length)])
    array2 = np.array([randint(1, 100) for _ in range(array_length)])

    max_values = np.maximum(array1, array2)

    fig, ax = plt.subplots()
    ax.plot(max_values)
    ax.set_ylabel('Maximum Values')

    assert ax.get_ylabel() == 'Maximum Values'
    assert len(ax.get_xdata()) == array_length
    assert len(ax.get_ydata()) == array_length
    assert np.all(ax.get_ydata() == max_values)