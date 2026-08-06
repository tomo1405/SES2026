import pytest
from src_0318 import task_func

def test_task_func():
    example_str = "This is an example string with some [brackets]."
    expected_output = {'example': 0.5772151898110195, 'string': 0.4629100498860761, 'with': 0.4629100498860761, 'some': 0.4629100498860761, 'brackets': 0.4629100498860761}
    actual_output = task_func(example_str)
    assert actual_output == expected_output

def test_task_func_empty_string():
    example_str = ""
    expected_output = {}
    actual_output = task_func(example_str)
    assert actual_output == expected_output

def test_task_func_no_brackets():
    example_str = "This is a string without any brackets."
    expected_output = {'this': 0.2876820724517809, 'is': 0.2876820724517809, 'a': 0.2876820724517809, 'string': 0.2876820724517809, 'without': 0.2876820724517809, 'any': 0.2876820724517809, 'brackets': 0.2876820724517809}
    actual_output = task_func(example_str)
    assert actual_output == expected_output