import pytest
from src_0661 import task_func
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler

def test_task_func():
    x = [np.array([1, 2, 3]), np.array([4, 5, 6])]
    y = [np.array([1, 2, 3]), np.array([4, 5, 6])]
    labels = ['label1', 'label2']

    fig = task_func(x, y, labels)

    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 1
    assert len(fig.axes[0].lines) == 2
    assert fig.axes[0].lines[0].get_label() == 'label1'
    assert fig.axes[0].lines[1].get_label() == 'label2'