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
    dest_dir = 'test_dir'
    expected_dest = os.path.join(dest_dir, filename)
    try:
        os.remove(filename)
    except FileNotFoundError:
        pass
    try:
        os.rmdir(dest_dir)
    except FileNotFoundError:
        pass
    actual_dest = task_func(filename, dest_dir)
    assert actual_dest == expected_dest
    assert os.path.isfile(actual_dest)
    assert os.path.isfile(filename)
    assert os.path.getsize(actual_dest) == os.path.getsize(filename)
    assert os.path.dirname(actual_dest) == os.path.abspath(dest_dir)

    # Test case 2: Copy a file to an existing directory
    filename = 'test.txt'
    dest_dir = 'test_dir'
    expected_dest = os.path.join(dest_dir, filename)
    try:
        os.remove(filename)
    except FileNotFoundError:
        pass
    os.mkdir(dest_dir)
    actual_dest = task_func(filename, dest_dir)
    assert actual_dest == expected_dest
    assert os.path.isfile(actual_dest)
    assert os.path.isfile(filename)
    assert os.path.getsize(actual_dest) == os.path.getsize(filename)
    assert os.path.dirname(actual_dest) == os.path.abspath(dest_dir)

    # Test case 3: Copy a file to a non-existent directory
    filename = 'test.txt'
    dest_dir = 'test_dir'
    expected_dest = os.path.join(dest_dir, filename)
    try:
        os.remove(filename)
    except FileNotFoundError:
        pass
    try:
        os.rmdir(dest_dir)
    except FileNotFoundError:
        pass
    with pytest.raises(OSError):
        task_func(filename, dest_dir)

    # Test case 4: Copy a file to a directory with a file with the same name
    filename = 'test.txt'
    dest_dir = 'test_dir'
    expected_dest = os.path.join(dest_dir, filename)
    try:
        os.remove(filename)
    except FileNotFoundError:
        pass
    os.mkdir(dest_dir)
    with open(filename, 'w') as f:
        f.write('test')
    with pytest.raises(shutil.SameFileError):
        task_func(filename, dest_dir)

    # Test case 5: Copy a file to a directory with a file with the same name and overwrite=True
    filename = 'test.txt'
    dest_dir = 'test_dir'
    expected_dest = os.path.join(dest_dir, filename)
    try:
        os.remove(filename)
    except FileNotFoundError:
        pass
    os.mkdir(dest_dir)
    with open(filename, 'w') as f:
        f.write('test')
    actual_dest = task_func(filename, dest_dir, overwrite=True)
    assert actual_dest == expected_dest
    assert os.path.isfile(actual_dest)
    assert os.path.isfile(filename)
    assert os.path.getsize(actual_dest) == os.path.getsize(filename)
    assert os.path.dirname(actual_dest) == os.path.abspath(dest_dir)

    # Test case 6: Copy a file to a directory with a file with the same name and overwrite=False
    filename = 'test.txt'
    dest_dir = 'test_dir'
    expected_dest = os.path.join(dest_dir, filename)
    try:
        os.remove(filename)
    except FileNotFoundError:
        pass
    os.mkdir(dest_dir)
    with open(filename, 'w') as f:
        f.write('test')
    with pytest.raises(FileExistsError):
        task_func(filename, dest_dir)