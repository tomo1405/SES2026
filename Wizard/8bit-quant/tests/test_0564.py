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
    filepath = 'C:/path/to/my/library.dll'
    destination_dir = 'C:/path/to/my/destination/directory'

    # Test if the function returns the correct value
    assert task_func(filepath, destination_dir) == 'my_library.dll'

    # Test if the function moves all the DLL files to the destination directory
    dll_dir = os.path.dirname(filepath)
    dll_files = glob.glob(os.path.join(dll_dir, '*.dll'))
    for dll_file in dll_files:
        assert os.path.isfile(os.path.join(destination_dir, os.path.basename(dll_file)))