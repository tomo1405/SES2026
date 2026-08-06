import pytest
from src_0726 import task_func


def test_task_func_with_default_args():
    task_func()

def test_task_func_with_custom_args():
    directory = '/path/to/custom/directory/'
    from_encoding = 'utf-8'
    to_encoding = 'ascii'
    task_func(directory, from_encoding, to_encoding)

def test_task_func_with_nonexistent_directory():
    directory = '/path/to/nonexistent/directory/'
    with pytest.raises(FileNotFoundError):
        task_func(directory)

def test_task_func_with_invalid_encoding():
    from_encoding = 'invalid_encoding'
    with pytest.raises(LookupError):
        task_func(from_encoding=from_encoding)