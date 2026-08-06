python
import pytest
from src_0660 import task_func

def test_task_func():
    x = [np.arange(0, 1, 0.01), np.arange(0, 1, 0.01)]
    y = [np.random.normal(0, 1, 100), np.random.normal(0, 1, 100)]
    labels = ['Group 1', 'Group 2']
    fig = task_func(x, y, labels)
    assert isinstance(fig, plt.Figure)