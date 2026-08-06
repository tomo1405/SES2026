python
import os
import errno
import shutil
import pytest

def task_func(filename, dest_dir):
    # Ensure the destination directory exists
    try:
        os.makedirs(dest_dir, exist_ok=True)  # Simplified directory creation
    except OSError as e:
        # Reraise the exception if it's not related to existing directory
        if e.errno != errno.EEXIST:
            raise

    # Copy the file
    dest = shutil.copy(filename, dest_dir)

    # Erase the original file content by opening in write mode and closing it
    with open(filename, 'w') as original_file:
        original_file.truncate(0)

    return os.path.abspath(dest)

def test_task_func():
    # Test case 1: Copy a file to a new directory
    filename = 'test.txt'
    dest_dir = 'new_dir'
    expected_dest = os.path.join(dest_dir, filename)
    with open(filename, 'w') as f:
        f.write('test')
    actual_dest = task_func(filename, dest_dir)
    assert actual_dest == expected_dest
    assert os.path.isfile(actual_dest)
    assert not os.path.isfile(filename)

    # Test case 2: Copy a file to an existing directory
    filename = 'test.txt'
    dest_dir = 'new_dir'
    expected_dest = os.path.join(dest_dir, filename)
    os.makedirs(dest_dir, exist_ok=True)
    with open(filename, 'w') as f:
        f.write('test')
    actual_dest = task_func(filename, dest_dir)
    assert actual_dest == expected_dest
    assert os.path.isfile(actual_dest)
    assert not os.path.isfile(filename)

    # Test case 3: Copy a file to a non-existing directory
    filename = 'test.txt'
    dest_dir = 'non_existing_dir'
    expected_dest = os.path.join(dest_dir, filename)
    with open(filename, 'w') as f:
        f.write('test')
    actual_dest = task_func(filename, dest_dir)
    assert actual_dest == expected_dest
    assert os.path.isfile(actual_dest)
    assert not os.path.isfile(filename)

    # Test case 4: Copy a file to a directory with invalid permissions
    filename = 'test.txt'
    dest_dir = '/root'
    expected_dest = os.path.join(dest_dir, filename)
    with open(filename, 'w') as f:
        f.write('test')
    with pytest.raises(PermissionError):
        task_func(filename, dest_dir)

    # Test case 5: Copy a file to a directory with a file with the same name
    filename = 'test.txt'
    dest_dir = 'new_dir'
    expected_dest = os.path.join(dest_dir, filename)
    os.makedirs(dest_dir, exist_ok=True)
    with open(filename, 'w') as f:
        f.write('test')
    with open(os.path.join(dest_dir, filename), 'w') as f:
        f.write('test')
    actual_dest = task_func(filename, dest_dir)
    assert actual_dest == expected_dest
    assert os.path.isfile(actual_dest)
    assert not os.path.isfile(filename)