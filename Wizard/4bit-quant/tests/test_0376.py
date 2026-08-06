python
import pytest
from src_0376 import task_func

def test_task_func():
    # Test case 1
    l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ax = task_func(l)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == 'First Principal Component'
    assert ax.get_ylabel() == 'Second Principal Component'
    assert ax.get_title() == 'PCA Result'

    # Test case 2
    l = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    ax = task_func(l)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == 'First Principal Component'
    assert ax.get_ylabel() == 'Second Principal Component'
    assert ax.get_title() == 'PCA Result'

    # Test case 3
    l = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
    ax = task_func(l)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == 'First Principal Component'
    assert ax.get_ylabel() == 'Second Principal Component'
    assert ax.get_title() == 'PCA Result'