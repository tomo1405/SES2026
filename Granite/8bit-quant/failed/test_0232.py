import pytest
from src_0232 import task_func

def test_task_func_with_no_objects():
    obj_list = []
    expected_ax = None
    actual_ax = task_func(obj_list)
    assert actual_ax == expected_ax

def test_task_func_with_one_object():
    obj_list = [ValueObject()]
    expected_ax = None
    actual_ax = task_func(obj_list)
    assert actual_ax == expected_ax

def test_task_func_with_multiple_objects():
    obj_list = [ValueObject() for _ in range(10)]
    expected_ax = None
    actual_ax = task_func(obj_list)
    assert actual_ax == expected_ax