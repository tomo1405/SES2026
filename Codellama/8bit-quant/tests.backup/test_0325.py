import pytest
from src_0325 import task_func

def test_task_func():
    file_list = ['file1.txt', 'file2.txt', 'file3.txt']
    exit_codes = task_func(file_list)
    assert len(exit_codes) == 3
    assert all(exit_code == 0 for exit_code in exit_codes)