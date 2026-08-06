import pytest
from src_0455 import task_func

def test_task_func_valid_input():
    src_dir = 'src'
    dest_dir = 'dest'
    ext = 'txt'
    files_moved = task_func(src_dir, dest_dir, ext)
    assert len(files_moved) == 2
    assert os.path.exists(os.path.join(dest_dir, 'file1.txt'))
    assert os.path.exists(os.path.join(dest_dir, 'file2.txt'))

def test_task_func_invalid_input():
    src_dir = 'src'
    dest_dir = 'dest'
    ext = 'txt'
    with pytest.raises(FileNotFoundError):
        task_func(src_dir, dest_dir, ext)