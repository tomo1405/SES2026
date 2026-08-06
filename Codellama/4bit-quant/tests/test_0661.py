import pytest
from src_0661 import task_func
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler

def test_task_func():
    # Test with valid input
    x = [[1, 2, 3], [4, 5, 6]]
    y = [[7, 8, 9], [10, 11, 12]]
    labels = ['label1', 'label2']
    fig = task_func(x, y, labels)
    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 1
    ax = fig.axes[0]
    assert len(ax.lines) == 2
    assert ax.get_legend() is not None

    # Test with invalid input
    with pytest.raises(ValueError):
        task_func(x, y, labels, invalid_input=True)