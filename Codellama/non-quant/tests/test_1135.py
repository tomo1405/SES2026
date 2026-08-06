import pytest
from src_1135 import task_func

def test_task_func_valid_input():
    source_dir = 'tests/test_data/source'
    target_dir = 'tests/test_data/target'
    prefix = '#Hash: '
    expected_files = [
        'tests/test_data/target/file1.txt',
        'tests/test_data/target/file2.txt',
        'tests/test_data/target/file3.txt'
    ]

    new_files = task_func(source_dir, target_dir, prefix)

    assert new_files == expected_files

def test_task_func_invalid_input():
    source_dir = 'tests/test_data/source'
    target_dir = 'tests/test_data/target'
    prefix = '#Hash: '

    with pytest.raises(FileNotFoundError):
        task_func(source_dir, target_dir, prefix)