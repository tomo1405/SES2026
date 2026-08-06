import pytest
from src_0318 import task_func

def test_task_func():
    example_str = "This is an example string with some [brackets]."
    expected_output = {'example': 0.2876820724517809, 'string': 0.2876820724517809, 'with': 0.2876820724517809, 'some': 0.2876820724517809, 'brackets': 0.2876820724517809}
    actual_output = task_func(example_str)
    assert actual_output == expected_output

def test_task_func_with_empty_string():
    example_str = ""
    expected_output = {}
    actual_output = task_func(example_str)
    assert actual_output == expected_output