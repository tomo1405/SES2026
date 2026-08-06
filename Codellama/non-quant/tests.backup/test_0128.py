import pytest
from src_0128 import task_func

def test_task_func():
    ROOT_DIR = 'test_root_dir'
    DEST_DIR = 'test_dest_dir'
    SPECIFIC_HASH = 'test_hash'

    files_moved = task_func(ROOT_DIR, DEST_DIR, SPECIFIC_HASH)

    assert files_moved == 0