import pytest
from src_0123 import task_func

def test_task_func():
    my_list = [1, 2, 3]
    random_array = task_func(my_list)
    assert len(random_array) == sum(my_list)
    assert all(random_array >= 0)
    assert all(random_array <= 1)