import pytest
from src_0784 import task_func

def test_task_func():
    src_dir = 'src_dir'
    dest_dir = 'dest_dir'
    extension = '.txt'

    files_moved = task_func(src_dir, dest_dir, extension)

    assert files_moved == 0

def test_task_func_with_files():
    src_dir = 'src_dir'
    dest_dir = 'dest_dir'
    extension = '.txt'

    files_moved = task_func(src_dir, dest_dir, extension)

    assert files_moved == 0

def test_task_func_with_invalid_extension():
    src_dir = 'src_dir'
    dest_dir = 'dest_dir'
    extension = '.exe'

    files_moved = task_func(src_dir, dest_dir, extension)

    assert files_moved == 0