import pytest
from src_0818 import task_func
import logging

def test_task_func_valid_input():
    letter_list = ['a', 'b', 'c', 'a', 'b']
    element = 'a'
    log_path = '.'
    result = task_func(letter_list=letter_list, element=element, log_path=log_path)
    assert result == 2

def test_task_func_invalid_input():
    letter_list = ['x', 'y', 'z']
    element = 'a'
    log_path = '.'
    with pytest.raises(ValueError):
        task_func(letter_list=letter_list, element=element, log_path=log_path)

def test_logging():
    letter_list = ['a', 'b', 'c', 'a', 'b']
    element = 'a'
    log_path = '.'
    task_func(letter_list=letter_list, element=element, log_path=log_path)
    with open('task_func.log', 'r') as log_file:
        log_content = log_file.read()
    assert "Function called with list" in log_content
    assert "Frequency of 'a' is 2" in log_content