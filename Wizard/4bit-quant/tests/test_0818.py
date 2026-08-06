python
import logging
import pytest
from src_0818 import task_func

def test_task_func():
    letter_list = ['a', 'b', 'c', 'd', 'e']
    element = 'd'
    log_path = 'logs'

    # Test case 1: element is in the letter list
    assert task_func(letter_list, element, log_path) == 1

    # Test case 2: element is not in the letter list
    with pytest.raises(ValueError):
        task_func(letter_list, 'f', log_path)