import pytest
from src_0770 import task_func

def test_task_func_single_item():
    assert task_func([['apple']]) == 'apple'

def test_task_func_multiple_items():
    assert task_func([['apple', 'banana'], ['banana', 'cherry']]) == 'banana'

def test_task_func_tie_breaker():
    assert task_func([['apple', 'banana'], ['banana', 'apple']]) == 'apple'

def test_task_func_empty_list():
    with pytest.raises(ValueError):
        task_func([])

def test_task_func_empty_sublists():
    assert task_func([[], [], []]) == None

def test_task_func_unique_items():
    assert task_func([['apple'], ['banana'], ['cherry']]) == 'apple'

def test_task_func_case_sensitive():
    assert task_func([['apple'], ['Apple']]) == 'apple'