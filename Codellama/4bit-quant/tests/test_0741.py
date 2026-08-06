import pytest
from src_0741 import task_func

def test_task_func():
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    assert task_func(my_dict) == ['c', 'b', 'a']

def test_task_func_empty_dict():
    my_dict = {}
    assert task_func(my_dict) == []

def test_task_func_invalid_input():
    my_dict = {'a': 'b'}
    with pytest.raises(ValueError):
        task_func(my_dict)