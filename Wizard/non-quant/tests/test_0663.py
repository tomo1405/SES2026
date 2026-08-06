python
import numpy as np
import matplotlib.pyplot as plt
import pytest
from src_0663 import task_func

def test_task_func():
    x = np.array([[1, 2], [3, 4], [5, 6]])
    y = np.array([[7, 8], [9, 10], [11, 12]])
    labels = ['A', 'B', 'C']

    fig = task_func(x, y, labels)

    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 1
    assert isinstance(fig.axes[0], plt.Axes)
    assert len(fig.axes[0].lines) == 3
    assert fig.axes[0].lines[0].get_label() == 'A'
    assert fig.axes[0].lines[1].get_label() == 'B'
    assert fig.axes[0].lines[2].get_label() == 'C'