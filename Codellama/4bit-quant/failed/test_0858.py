import pytest
from src_0858 import task_func

def test_task_func():
    # Test that the function returns a list of transferred files
    transferred_files = task_func('source_dir', 'dest_dir', ['txt', 'pdf'])
    assert isinstance(transferred_files, list)
    assert len(transferred_files) == 2

    # Test that the function raises an exception when the source directory does not exist
    with pytest.raises(FileNotFoundError):
        task_func('invalid_source_dir', 'dest_dir', ['txt', 'pdf'])

    # Test that the function raises an exception when the destination directory does not exist
    with pytest.raises(FileNotFoundError):
        task_func('source_dir', 'invalid_dest_dir', ['txt', 'pdf'])

    # Test that the function raises an exception when the file extension is not supported
    with pytest.raises(ValueError):
        task_func('source_dir', 'dest_dir', ['invalid_ext'])

    # Test that the function raises an exception when the file cannot be moved
    with pytest.raises(Exception):
        task_func('source_dir', 'dest_dir', ['txt', 'pdf'])

    # Test that the function logs a warning when a file cannot be moved
    with pytest.warns(UserWarning):
        task_func('source_dir', 'dest_dir', ['txt', 'pdf'])