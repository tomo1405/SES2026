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
    filepath = "path/to/file.dll"
    destination_dir = "path/to/destination"
    expected_output = "library_name"

    actual_output = task_func(filepath, destination_dir)

    assert actual_output == expected_output, "Output does not match expected output"