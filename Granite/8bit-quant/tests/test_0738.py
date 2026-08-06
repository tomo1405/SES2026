import pytest
from src_0738 import task_func

def test_task_func():
    with pytest.raises(ValueError):
        task_func([])

def test_task_func_with_even_length_list():
    assert task_func([1, 2, 3, 4]) == 2.5

def test_task_func_with_odd_length_list():
    assert task_func([1, 2, 3, 4, 5]) == 3