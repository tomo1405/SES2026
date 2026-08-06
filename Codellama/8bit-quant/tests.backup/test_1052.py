import pytest
from src_1052 import task_func

def test_task_func_empty_dict():
    ax, message = task_func({})
    assert ax is None
    assert message == "The distribution is uniform."

def test_task_func_uniform_distribution():
    data_dict = {1: 10, 2: 10, 3: 10, 4: 10, 5: 10}
    ax, message = task_func(data_dict)
    assert ax is not None
    assert message == "The distribution is uniform."

def test_task_func_non_uniform_distribution():
    data_dict = {1: 10, 2: 10, 3: 10, 4: 10, 5: 11}
    ax, message = task_func(data_dict)
    assert ax is not None
    assert message == "The distribution is not uniform."