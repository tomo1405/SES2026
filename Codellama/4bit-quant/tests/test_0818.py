import pytest
from src_0818 import task_func

def test_task_func():
    letter_list = ['a', 'b', 'c', 'd', 'e']
    element = 'a'
    log_path = 'path/to/log/file'

    with pytest.raises(ValueError):
        task_func(letter_list, 'f', log_path)

    assert task_func(letter_list, element, log_path) == 1