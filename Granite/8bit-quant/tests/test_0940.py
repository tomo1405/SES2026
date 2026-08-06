import re
import os
import glob
import pytest

def task_func(dir_path: str) -> list:
    new_names = []
    for file_path in glob.glob(os.path.join(dir_path, '*')):
        base_name = os.path.basename(file_path)
        new_name = re.sub('[^A-Za-z0-9]+', '', base_name)
        new_path = os.path.join(dir_path, new_name)
        os.rename(file_path, new_path)
        new_names.append(new_name)
    return new_names

def test_task_func():
    dir_path = '/path/to/directory'
    new_names = task_func(dir_path)
    assert isinstance(new_names, list)
    for name in new_names:
        assert isinstance(name, str)