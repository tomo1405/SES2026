import pytest
from src_0282 import task_func

def test_task_func():
    folder_path = 'path/to/folder'
    expected_result = {'192.168.1.1': 2, '192.168.1.2': 3, '192.168.1.3': 4}
    result = task_func(folder_path)
    assert result == expected_result