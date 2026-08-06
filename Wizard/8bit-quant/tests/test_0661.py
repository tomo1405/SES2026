python
import pytest
from src_0661 import task_func

def test_task_func():
    # Test case 1: Test with 2 datasets
    x = [np.array([1, 2, 3]), np.array([4, 5, 6])]
    y = [np.array([1, 2, 3]), np.array([4, 5, 6])]
    labels = ['Dataset 1', 'Dataset 2']
    fig = task_func(x, y, labels)
    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 1
    assert len(fig.axes[0].lines) == 2
    assert fig.axes[0].lines[0].get_label() == 'Dataset 1'
    assert fig.axes[0].lines[1].get_label() == 'Dataset 2'

    # Test case 2: Test with 1 dataset
    x = [np.array([1, 2, 3])]
    y = [np.array([1, 2, 3])]
    labels = ['Dataset 1']
    fig = task_func(x, y, labels)
    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 1
    assert len(fig.axes[0].lines) == 1
    assert fig.axes[0].lines[0].get_label() == 'Dataset 1'

    # Test case 3: Test with empty dataset
    x = []
    y = []
    labels = []
    fig = task_func(x, y, labels)
    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 1
    assert len(fig.axes[0].lines) == 0