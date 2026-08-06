python
import ctypes
import os
import shutil
import glob
import pytest

def task_func(filepath, destination_dir):
    lib = ctypes.CDLL(filepath)

    dll_dir = os.path.dirname(filepath)
    dll_files = glob.glob(os.path.join(dll_dir, '*.dll'))

    for dll_file in dll_files:
        shutil.move(dll_file, destination_dir)

    return lib._name

def test_task_func():
    filepath = 'C:/Users/user/Documents/my_dll.dll'
    destination_dir = 'C:/Users/user/Documents/my_dll_folder'

    # Test if the function returns the correct value
    assert task_func(filepath, destination_dir) == 'my_dll.dll'

    # Test if the function moves all the dll files to the destination directory
    assert os.path.exists(os.path.join(destination_dir, 'my_dll.dll'))
    assert not os.path.exists(os.path.join(dll_dir, 'my_dll.dll'))

    # Test if the function does not move any files if the destination directory does not exist
    destination_dir = 'C:/Users/user/Documents/non_existent_folder'
    assert task_func(filepath, destination_dir) == 'my_dll.dll'
    assert not os.path.exists(os.path.join(destination_dir, 'my_dll.dll'))