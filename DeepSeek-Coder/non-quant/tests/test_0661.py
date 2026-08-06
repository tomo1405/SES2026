import pytest
from src_0661 import task_func
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Mock data for testing
x = [np.array([[1, 2], [3, 4]]), np.array([[5, 6], [7, 8]])]
y = [np.array([1, 2]), np.array([3, 4])]
labels = ["Dataset 1", "Dataset 2"]

def test_task_func():
    fig = task_func(x, y, labels)
    assert isinstance(fig, plt.Figure)
    assert len(fig.get_axes()) == 1
    assert len(fig.get_axes()[0].get_lines()) == 2