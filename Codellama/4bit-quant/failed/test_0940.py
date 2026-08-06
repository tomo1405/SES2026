import pytest
from src_0940 import task_func

def test_task_func():
    dir_path = 'path/to/directory'
    new_names = task_func(dir_path)
    assert len(new_names) == 3
    assert new_names[0] == 'file1.txt'
    assert new_names[1] == 'file2.txt'
    assert new_names[2] == 'file3.txt'