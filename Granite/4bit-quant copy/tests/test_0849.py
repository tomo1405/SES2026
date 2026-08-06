import heapq
import random
import pytest

from src_0849 import task_func

def test_task_func():
    obj_list = [object() for _ in range(10)]
    attr = 'attr'
    top_n = 5
    seed = 42

    top_values, random_value = task_func(obj_list, attr, top_n, seed)

    assert len(top_values) == top_n
    assert random_value in [getattr(obj, attr) for obj in obj_list]

def test_task_func_with_empty_obj_list():
    obj_list = []
    attr = 'attr'
    top_n = 5
    seed = 42

    top_values, random_value = task_func(obj_list, attr, top_n, seed)

    assert len(top_values) == 0
    assert random_value is None

def test_task_func_with_negative_top_n():
    obj_list = [object() for _ in range(10)]
    attr = 'attr'
    top_n = -1
    seed = 42

    with pytest.raises(ValueError):
        task_func(obj_list, attr, top_n, seed)