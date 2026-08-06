import pytest
from src_0756 import task_func

def test_task_func():
    directory_path = 'path/to/directory'
    new_filenames = task_func(directory_path)
    assert len(new_filenames) == 2
    assert new_filenames[0] == 'file1.txt'
    assert new_filenames[1] == 'file2.txt'