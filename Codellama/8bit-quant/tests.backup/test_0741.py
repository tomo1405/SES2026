import pytest
from src_0741 import task_func

def test_task_func():
    my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    expected_result = ['e', 'd', 'c']
    assert task_func(my_dict) == expected_result

def test_task_func_empty_dict():
    my_dict = {}
    expected_result = []
    assert task_func(my_dict) == expected_result

def test_task_func_invalid_input():
    my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    with pytest.raises(TypeError):
        task_func(my_dict, 10)