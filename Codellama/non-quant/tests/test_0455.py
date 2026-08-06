import pytest
from src_0455 import task_func

def test_task_func_valid_input():
    src_dir = 'src'
    dest_dir = 'dest'
    ext = 'txt'
    files_moved = task_func(src_dir, dest_dir, ext)
    assert len(files_moved) == 2
    assert files_moved[0] == 'dest/file1.txt'
    assert files_moved[1] == 'dest/file2.txt'

def test_task_func_invalid_input():
    src_dir = 'src'
    dest_dir = 'dest'
    ext = 'txt'
    with pytest.raises(FileNotFoundError):
        task_func(src_dir, dest_dir, ext)