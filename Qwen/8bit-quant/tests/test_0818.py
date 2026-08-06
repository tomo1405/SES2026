import pytest
from src_0818 import task_func
import os
import logging

@pytest.fixture
def setup_logger(tmpdir):
    log_path = tmpdir.mkdir("logs")
    return str(log_path)

def test_task_func_element_in_list(setup_logger):
    letter_list = ['a', 'b', 'c', 'a', 'b', 'a']
    element = 'a'
    expected_frequency = 3
    actual_frequency = task_func(letter_list, element, setup_logger)
    assert actual_frequency == expected_frequency

    # Check log file content
    with open(os.path.join(setup_logger, 'task_func.log'), 'r') as log_file:
        log_content = log_file.read()
        assert "INFO:Function called with list: ['a', 'b', 'c', 'a', 'b', 'a'] and element: a" in log_content
        assert "INFO:Frequency of 'a' is 3" in log_content

def test_task_func_element_not_in_list(setup_logger):
    letter_list = ['a', 'b', 'c']
    element = 'd'
    with pytest.raises(ValueError) as excinfo:
        task_func(letter_list, element, setup_logger)
    assert str(excinfo.value) == "The element is not in the letter list."

    # Check log file content
    with open(os.path.join(setup_logger, 'task_func.log'), 'r') as log_file:
        log_content = log_file.read()
        assert "INFO:Function called with list: ['a', 'b', 'c'] and element: d" in log_content
        assert "ERROR:The element is not in the letter list." in log_content

def test_task_func_empty_list(setup_logger):
    letter_list = []
    element = 'a'
    with pytest.raises(ValueError) as excinfo:
        task_func(letter_list, element, setup_logger)
    assert str(excinfo.value) == "The element is not in the letter list."

    # Check log file content
    with open(os.path.join(setup_logger, 'task_func.log'), 'r') as log_file:
        log_content = log_file.read()
        assert "INFO:Function called with list: [] and element: a" in log_content
        assert "ERROR:The element is not in the letter list." in log_content

def test_task_func_single_element_list(setup_logger):
    letter_list = ['x']
    element = 'x'
    expected_frequency = 1
    actual_frequency = task_func(letter_list, element, setup_logger)
    assert actual_frequency == expected_frequency

    # Check log file content
    with open(os.path.join(setup_logger, 'task_func.log'), 'r') as log_file:
        log_content = log_file.read()
        assert "INFO:Function called with list: ['x'] and element: x" in log_content
        assert "INFO:Frequency of 'x' is 1" in log_content