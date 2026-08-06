import pytest
from src_0232 import task_func

def test_task_func():
    # Create a list of ValueObject instances
    obj_list = [ValueObject(mu=5, std=2, seed=123) for _ in range(10)]
    ax = task_func(obj_list=obj_list)
    assert ax is not None