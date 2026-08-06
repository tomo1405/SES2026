import pytest
from src_0770 import task_func

def test_task_func_single_item():
    assert task_func([['apple']]) == 'apple'

def test_task_func_multiple_items():
    assert task_func([['apple', 'banana'], ['apple']]) == 'apple'

def test_task_func_tie_breaker():
    assert task_func([['apple', 'banana'], ['banana', 'apple']]) == 'apple'

def test_task_func_empty_list():
    with pytest.raises(ValueError):
        task_func([])

def test_task_func_empty_sublists():
    assert task_func([[], []]) is None

def test_task_func_mixed_types():
    assert task_func([['apple', 1], [1, 'apple']]) == 'apple'

def test_task_func_large_input():
    large_list = [['apple'] * 1000, ['banana'] * 500, ['cherry'] * 250]
    assert task_func(large_list) == 'apple'