import pytest
from src_0116 import task_func

def test_task_func():
    numbers = [1, 2, 3, 4, 5]
    my_dict = task_func(numbers)
    assert my_dict['mode'] == 3
    assert my_dict['entropy'] == 1.5849625007211563

def test_task_func_empty_list():
    numbers = []
    with pytest.raises(ValueError):
        task_func(numbers)

def test_task_func_invalid_input():
    numbers = [1, 2, 3, 4, 5, 'a']
    with pytest.raises(ValueError):
        task_func(numbers)