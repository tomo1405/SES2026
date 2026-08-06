import pytest
from src_0818 import task_func
from collections import Counter
import logging

@pytest.fixture
def setup_logging():
    formatter = logging.Formatter('%(levelname)s:%(message)s')
    handler = logging.FileHandler('task_func.log', mode='w')
    logger = logging.getLogger()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    yield logger
    logger.handlers[0].close()
    logger.removeHandler(logger.handlers[0])
    logging.shutdown()

def test_task_func_with_element_in_letter_list(setup_logging):
    letter_list = ['a', 'b', 'c', 'd', 'e']
    element = 'd'
    expected_output = 1
    actual_output = task_func(letter_list, element, 'logs')
    assert actual_output == expected_output

def test_task_func_with_element_not_in_letter_list(setup_logging):
    letter_list = ['a', 'b', 'c', 'd', 'e']
    element = 'f'
    with pytest.raises(ValueError) as excinfo:
        task_func(letter_list, element, 'logs')
    assert "The element is not in the letter list." in str(excinfo.value)

def test_task_func_with_element_in_letter_list_and_logging(setup_logging):
    letter_list = ['a', 'b', 'c', 'd', 'e']
    element = 'd'
    with open('logs/task_func.log', 'r') as log_file:
        log_lines = log_file.readlines()
    expected_log_lines = [
        'DEBUG:Function called with list: ['a', 'b', 'c', 'd', 'e'] and element: d\n',
        'INFO:Frequency of \'d\' is 1\n'
    ]
    assert log_lines == expected_log_lines