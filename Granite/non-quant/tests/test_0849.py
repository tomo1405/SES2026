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