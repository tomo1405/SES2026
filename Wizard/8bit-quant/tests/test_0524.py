python
import pytest
from src_0524 import task_func

def test_task_func():
    # Test case 1: Empty data
    assert task_func([]) is None
    
    # Test case 2: Valid data
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == 'Time'
    assert ax.get_ylabel() == 'Data Points'
    assert ax.get_title() == 'Data over Time'
    assert ax.get_legend_handles_labels() == ([], [])
    plt.close()