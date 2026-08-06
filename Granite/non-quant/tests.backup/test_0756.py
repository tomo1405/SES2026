import os
import glob
import pytest

def task_func(directory_path):
    new_filenames = []
    for filename in glob.glob(os.path.join(directory_path, '*')):
        base_name = os.path.basename(filename)
        new_base_name = '.'.join(base_name.split('.')[::-1])
        os.rename(filename, os.path.join(directory_path, new_base_name))
        new_filenames.append(new_base_name)
    return new_filenames

def test_task_func():
    directory_path = '/path/to/directory'
    new_filenames = task_func(directory_path)
    assert len(new_filenames) > 0
    for filename in new_filenames:
        assert filename.count('.') == 1
        assert os.path.exists(os.path.join(directory_path, filename))