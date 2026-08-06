python
import pytest
from src_0318 import task_func

def test_task_func():
    example_str = "This is a test string [with some text] to test the task_func function."
    expected_result = {'test': 0.0, 'string': 0.0, 'with': 0.0, 'some': 0.0, 'text': 0.0}
    assert task_func(example_str) == expected_result