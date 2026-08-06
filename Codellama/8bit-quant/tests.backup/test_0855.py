import pytest
from src_0855 import task_func

def test_task_func_type_error():
    with pytest.raises(TypeError):
        task_func("not a list")

def test_task_func_value_error():
    with pytest.raises(ValueError):
        task_func([-1, 2, 3])

def test_task_func_empty_list():
    sums, permutations = task_func([])
    assert sums == []
    assert permutations == []

def test_task_func_valid_input():
    sums, permutations = task_func([1, 2, 3])
    assert sums == [6, 6, 6]
    assert permutations == [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]