import pytest
from src_0940 import task_func

def test_task_func():
    dir_path = 'test_dir'
    new_names = task_func(dir_path)
    assert new_names == ['file1', 'file2', 'file3']