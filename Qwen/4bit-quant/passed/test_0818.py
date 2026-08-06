import pytest
from src_0818 import task_func
import os
import logging

def test_task_func_element_in_list(tmpdir):
    # Create a temporary directory for the log file
    log_dir = tmpdir.mkdir("logs")
    log_path = str(log_dir)

    # Test case where the element is in the list
    letter_list = ['a', 'b', 'c', 'a', 'd']
    element = 'a'
    expected_frequency = 2

    frequency = task_func(letter_list, element, log_path)

    assert frequency == expected_frequency

    # Check if the log file was created and contains the correct information
    log_file_path = os.path.join(log_path, 'task_func.log')
    assert os.path.exists(log_file_path)

    with open(log_file_path, 'r') as log_file:
        log_content = log_file.read()
        assert "INFO:Function called with list: ['a', 'b', 'c', 'a', 'd'] and element: a" in log_content
        assert f"INFO:Frequency of 'a' is {expected_frequency}" in log_content

def test_task_func_element_not_in_list(tmpdir):
    # Create a temporary directory for the log file
    log_dir = tmpdir.mkdir("logs")
    log_path = str(log_dir)

    # Test case where the element is not in the list
    letter_list = ['a', 'b', 'c', 'd']
    element = 'e'

    with pytest.raises(ValueError) as excinfo:
        task_func(letter_list, element, log_path)

    assert str(excinfo.value) == "The element is not in the letter list."

    # Check if the log file was created and contains the correct error message
    log_file_path = os.path.join(log_path, 'task_func.log')
    assert os.path.exists(log_file_path)

    with open(log_file_path, 'r') as log_file:
        log_content = log_file.read()
        assert "INFO:Function called with list: ['a', 'b', 'c', 'd'] and element: e" in log_content
        assert "ERROR:The element is not in the letter list." in log_content