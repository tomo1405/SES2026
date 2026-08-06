python
import re
import pytest
from src_0941 import task_func

def test_task_func():
    input_str = "This is a sample input string"
    expected_output = {'a': 1, 'is': 1, 'sample': 1, 'input': 1, 'string': 1}
    assert task_func(input_str) == expected_output