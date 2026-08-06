import pytest
from src_0818 import task_func

def test_task_func():
    letter_list = ['a', 'b', 'c', 'a', 'b', 'a']
    element = 'a'
    log_path = '/path/to/log'
    expected_output = 3

    with pytest.raises(ValueError) as exc_info:
        task_func(letter_list, element, log_path)

    assert "The element is not in the letter list." in str(exc_info.value)

def test_task_func_with_element_in_list():
    letter_list = ['a', 'b', 'c', 'a', 'b', 'a']
    element = 'b'
    log_path = '/path/to/log'
    expected_output = 2

    actual_output = task_func(letter_list, element, log_path)

    assert actual_output == expected_output