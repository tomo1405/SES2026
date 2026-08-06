import pytest
from src_0128 import task_func


def test_task_func_with_valid_input():
    ROOT_DIR = 'tests/test_data'
    DEST_DIR = 'tests/test_data/dest'
    SPECIFIC_HASH = '00000000000000000000000000000000'

    files_moved = task_func(ROOT_DIR, DEST_DIR, SPECIFIC_HASH)

    assert files_moved == 1
    assert os.path.exists(os.path.join(DEST_DIR, 'file1.txt'))


def test_task_func_with_invalid_input():
    ROOT_DIR = 'tests/test_data'
    DEST_DIR = 'tests/test_data/dest'
    SPECIFIC_HASH = '11111111111111111111111111111111'

    files_moved = task_func(ROOT_DIR, DEST_DIR, SPECIFIC_HASH)

    assert files_moved == 0
    assert not os.path.exists(os.path.join(DEST_DIR, 'file1.txt'))