python
import pytest
from src_0367 import task_func

def test_task_func():
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    bins = 5
    ax = task_func(number_list, bins)
    assert ax.get_title() == 'Histogram'
    assert ax.get_xlabel() == 'Number'
    assert ax.get_ylabel() == 'Frequency'
    assert ax.get_xlim() == (0.5, 10.5)
    assert ax.get_ylim() == (0, 5)
    assert ax.patches[0].get_facecolor() == (0.0, 0.0, 1.0, 1.0)