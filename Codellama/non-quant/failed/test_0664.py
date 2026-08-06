import pytest
from src_0664 import task_func
import numpy as np

def test_task_func_empty_data():
    with pytest.raises(ValueError):
        task_func([], [], [])

def test_task_func_valid_data():
    x = np.array([1, 2, 3])
    y = np.array([4, 5, 6])
    labels = ['label1', 'label2', 'label3']
    fig = task_func(x, y, labels)
    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 1
    assert len(fig.axes[0].lines) == 3
    assert fig.axes[0].get_legend() is not None