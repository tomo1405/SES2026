import pytest
from src_0818 import task_func

def test_task_func_with_valid_input():
    letter_list = ['a', 'b', 'c', 'd', 'e']
    element = 'a'
    log_path = 'path/to/log/file'

    result = task_func(letter_list, element, log_path)

    assert result == 1

def test_task_func_with_invalid_input():
    letter_list = ['a', 'b', 'c', 'd', 'e']
    element = 'f'
    log_path = 'path/to/log/file'

    with pytest.raises(ValueError):
        task_func(letter_list, element, log_path)