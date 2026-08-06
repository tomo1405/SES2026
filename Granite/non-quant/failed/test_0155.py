import re
import os
import glob
import mimetypes
import pytest

def task_func(directory, file_pattern, suffix):
    os.chdir(directory)
    files = glob.glob(file_pattern)
    file_types = {}

    for file in files:
        if re.search(suffix, file):
            file_type = mimetypes.guess_type(file)[0]
            file_types[file] = file_type

    return file_types

def test_task_func():
    directory = "/path/to/directory"
    file_pattern = "*.txt"
    suffix = ".txt"
    expected_output = {
        "file1.txt": "text/plain",
        "file2.txt": "text/plain",
        "file3.txt": "text/plain"
    }
    actual_output = task_func(directory, file_pattern, suffix)
    assert actual_output == expected_output