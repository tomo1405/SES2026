python
import pytest
from src_0524 import task_func

def test_task_func_empty_data():
    assert task_func([]) is None

def test_task_func_valid_data():
    data = [[1, 2, 3], [4, 5, 6]]
    ax = task_func(data)
    assert ax.get_xlabel() == "Time"
    assert ax.get_ylabel() == "Data Points"
    assert ax.get_title() == "Data over Time"
    assert ax.get_legend_handles_labels()[0] == ['0', '1']