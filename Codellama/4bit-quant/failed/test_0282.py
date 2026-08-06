import pytest
from src_0282 import task_func

def test_task_func():
    folder_path = 'path/to/folder'
    expected_result = {'192.168.1.1': 2, '10.0.0.1': 3, '172.16.0.1': 1}
    result = task_func(folder_path)
    assert result == expected_result