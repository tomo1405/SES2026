import pytest
from src_1052 import task_func

def test_task_func():
    data_dict = {'A': 1, 'B': 2, 'C': 3}
    ax, message = task_func(data_dict)
    assert ax is not None
    assert message == "The distribution is uniform."

def test_task_func_with_non_uniform_distribution():
    data_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 1, 'E': 2, 'F': 3}
    ax, message = task_func(data_dict)
    assert ax is not None
    assert message == "The distribution is not uniform."