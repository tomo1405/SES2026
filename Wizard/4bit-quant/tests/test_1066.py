python
import pytest
import numpy as np
from src_1066 import task_func

def test_task_func():
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    ax = task_func(arr)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Absolute values of FFT coefficients"
    assert len(ax.lines) == 1
    assert len(ax.lines[0].get_data()[0]) == 3
    assert len(ax.lines[0].get_data()[1]) == 3
    assert ax.lines[0].get_data()[0][0] == 10.0
    assert ax.lines[0].get_data()[1][0] == 0.0
    assert ax.lines[0].get_data()[0][1] == 26.0
    assert ax.lines[0].get_data()[1][1] == 0.0
    assert ax.lines[0].get_data()[0][2] == 42.0
    assert ax.lines[0].get_data()[1][2] == 0.0