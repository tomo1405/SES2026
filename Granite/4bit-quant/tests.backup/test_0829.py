import os
import errno
import shutil
import pytest

def task_func(filename, dest_dir):
    try:
        os.makedirs(dest_dir, exist_ok=True)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    dest = shutil.copy(filename, dest_dir)

    with open(filename, 'w') as original_file:
        original_file.truncate(0)

    return os.path.abspath(dest)

def test_task_func():
    filename = "test_file.txt"
    dest_dir = "test_dir"
    expected_output = os.path.join(os.getcwd(), dest_dir, filename)

    # Test if the destination directory is created
    with pytest.raises(OSError) as exc_info:
        task_func(filename, dest_dir)
    assert exc_info.value.errno == errno.EEXIST

    # Test if the file is copied to the destination directory
    assert task_func(filename, dest_dir) == expected_output

    # Test if the original file content is erased
    with open(filename, 'r') as original_file:
        assert original_file.read() == ""