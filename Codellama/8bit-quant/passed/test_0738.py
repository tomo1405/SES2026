import pytest
from src_0738 import task_func

def test_task_func_empty_list():
    with pytest.raises(ValueError):
        task_func([])

def test_task_func_single_element_list():
    assert task_func([1]) == 1

def test_task_func_even_number_of_elements():
    assert task_func([1, 2, 3, 4]) == 2.5

def test_task_func_odd_number_of_elements():
    assert task_func([1, 2, 3, 4, 5]) == 3