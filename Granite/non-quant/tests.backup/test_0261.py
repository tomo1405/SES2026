import json
import os
import glob
from src_0261 import task_func

def test_task_func():
    directory = "/path/to/directory"
    updated_files = task_func(directory)
    assert isinstance(updated_files, int)
    assert updated_files >= 0

def test_task_func_with_no_files():
    directory = "/path/to/empty/directory"
    updated_files = task_func(directory)
    assert updated_files == 0

def test_task_func_with_one_file():
    directory = "/path/to/directory/with/one/file.json"
    updated_files = task_func(directory)
    assert updated_files == 1

def test_task_func_with_multiple_files():
    directory = "/path/to/directory/with/multiple/files.json"
    updated_files = task_func(directory)
    assert updated_files >= 1