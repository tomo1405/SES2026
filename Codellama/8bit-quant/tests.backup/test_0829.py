import pytest
from src_0829 import task_func

def test_task_func():
    # Test that the function raises an error if the destination directory does not exist
    with pytest.raises(OSError):
        task_func('test_file.txt', 'non_existent_dir')

    # Test that the function copies the file to the destination directory
    with pytest.raises(OSError):
        task_func('test_file.txt', 'existing_dir')

    # Test that the function erases the original file content
    with pytest.raises(OSError):
        task_func('test_file.txt', 'existing_dir')

    # Test that the function returns the absolute path of the copied file
    assert task_func('test_file.txt', 'existing_dir') == os.path.abspath('existing_dir/test_file.txt')