import pytest
from src_0328 import task_func

def test_task_func():
    file_path = 'test_data.csv'
    regex_pattern = r'\(.+?\)|\w+|[\W_]+'
    expected_result = {'hello': 2, 'world': 1, '!': 1}

    result = task_func(file_path, regex_pattern)

    assert result == expected_result