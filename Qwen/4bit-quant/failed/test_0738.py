import pytest
from src_0738 import task_func

def test_task_func_with_flat_list():
    assert task_func([3, 1, 4, 1, 5, 9]) == 3

def test_task_func_with_nested_list():
    assert task_func([[3, 1], [4, 1], [5, 9]]) == 3

def test_task_func_with_single_element():
    assert task_func([42]) == 42

def test_task_func_with_even_number_of_elements():
    assert task_func([1, 2, 3, 4]) == 2.5

def test_task_func_with_empty_list():
    with pytest.raises(ValueError):
        task_func([])

def test_task_func_with_negative_numbers():
    assert task_func([-5, -1, -3, -4]) == -3.5

def test_task_func_with_mixed_types():
    with pytest.raises(TypeError):
        task_func([1, 'a', 3])

def test_task_func_with_floats():
    assert task_func([1.5, 2.5, 3.5, 4.5]) == 3.0

def test_task_func_with_large_numbers():
    assert task_func([1000000, 2000000, 3000000]) == 2000000