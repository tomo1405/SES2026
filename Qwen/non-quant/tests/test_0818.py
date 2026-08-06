import pytest
from src_0818 import task_func
import os
import logging

@pytest.fixture
def setup_logger(tmpdir):
    log_path = str(tmpdir)
    return log_path

def test_element_in_list(setup_logger):
    letter_list = ['a', 'b', 'c', 'a', 'b', 'a']
    element = 'a'
    log_path = setup_logger
    result = task_func(letter_list, element, log_path)
    assert result == 3
    with open(os.path.join(log_path, 'task_func.log'), 'r') as f:
        logs = f.readlines()
    assert "INFO:Function called with list: ['a', 'b', 'c', 'a', 'b', 'a'] and element: a\n" in logs
    assert "INFO:Frequency of 'a' is 3\n" in logs

def test_element_not_in_list(setup_logger):
    letter_list = ['a', 'b', 'c']
    element = 'd'
    log_path = setup_logger
    with pytest.raises(ValueError) as excinfo:
        task_func(letter_list, element, log_path)
    assert str(excinfo.value) == "The element is not in the letter list."
    with open(os.path.join(log_path, 'task_func.log'), 'r') as f:
        logs = f.readlines()
    assert "INFO:Function called with list: ['a', 'b', 'c'] and element: d\n" in logs
    assert "ERROR:The element is not in the letter list.\n" in logs

def test_logging_configuration(setup_logger):
    letter_list = ['a', 'b', 'c', 'a', 'b', 'a']
    element = 'a'
    log_path = setup_logger
    task_func(letter_list, element, log_path)
    logger = logging.getLogger()
    assert not logger.hasHandlers()