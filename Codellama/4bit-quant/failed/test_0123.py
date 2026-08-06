import pytest
from src_0123 import task_func

def test_task_func():
    my_list = [1, 2, 3]
    random_array = task_func(my_list)
    assert len(random_array) == sum(my_list)
    assert all(random_array >= 0) and all(random_array <= 1)

def test_task_func_empty_list():
    my_list = []
    random_array = task_func(my_list)
    assert len(random_array) == 0

def test_task_func_invalid_input():
    my_list = [1, 2, 3]
    with pytest.raises(ValueError):
        task_func(my_list, 10)