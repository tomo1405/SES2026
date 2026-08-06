import pytest
from src_1052 import task_func

def test_task_func():
    data_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
    ax, message = task_func(data_dict)
    assert ax is not None
    assert message == "The distribution is uniform."

def test_task_func_empty_dict():
    data_dict = {}
    ax, message = task_func(data_dict)
    assert ax is None
    assert message == "The distribution is uniform."

def test_task_func_non_uniform():
    data_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
    ax, message = task_func(data_dict)
    assert ax is not None
    assert message == "The distribution is not uniform."