python
import pytest
from src_0330 import task_func

def test_task_func():
    file_path = 'data.json'
    regex_pattern = r'\(.+?\)|\w'
    expected_result = {'data.json': ['(hello)', 'world']}

    result = task_func(file_path, regex_pattern)

    assert result == expected_result