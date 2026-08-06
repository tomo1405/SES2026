python
import pytest
from src_0253 import task_func

def test_task_func():
    data = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    labels = ['A', 'B', 'C']
    ax = task_func(data, labels)
    assert ax.get_xlabel() == 'Index'
    assert ax.get_ylabel() == 'Value'
    assert ax.get_title() == 'Task Function'
    assert ax.get_legend_handles_labels()[1] == labels