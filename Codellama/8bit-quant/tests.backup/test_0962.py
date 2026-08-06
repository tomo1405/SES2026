import pytest
from src_0962 import task_func

def test_task_func_valid_directory():
    directory = "path/to/directory"
    extensions = [".txt", ".docx", ".xlsx", ".csv"]
    counter = task_func(directory, extensions)
    assert isinstance(counter, Counter)
    assert all(suffix in counter for suffix in extensions)

def test_task_func_invalid_directory():
    directory = "path/to/invalid/directory"
    extensions = [".txt", ".docx", ".xlsx", ".csv"]
    with pytest.raises(OSError):
        task_func(directory, extensions)

def test_task_func_keep_zero():
    directory = "path/to/directory"
    extensions = [".txt", ".docx", ".xlsx", ".csv"]
    counter = task_func(directory, extensions, keep_zero=True)
    assert isinstance(counter, Counter)
    assert all(suffix in counter for suffix in extensions)
    assert all(counter[suffix] >= 0 for suffix in extensions)

def test_task_func_no_keep_zero():
    directory = "path/to/directory"
    extensions = [".txt", ".docx", ".xlsx", ".csv"]
    counter = task_func(directory, extensions, keep_zero=False)
    assert isinstance(counter, Counter)
    assert all(suffix in counter for suffix in extensions)
    assert all(counter[suffix] > 0 for suffix in extensions)