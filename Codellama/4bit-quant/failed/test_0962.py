import pytest
from src_0962 import task_func

def test_task_func():
    directory = "path/to/directory"
    extensions = [".txt", ".docx", ".xlsx", ".csv"]
    keep_zero = True

    counter = task_func(directory, extensions, keep_zero)

    assert isinstance(counter, Counter)
    assert all(suffix in counter for suffix in extensions)
    assert all(counter[suffix] >= 0 for suffix in extensions)

def test_task_func_with_invalid_directory():
    directory = "path/to/invalid/directory"
    extensions = [".txt", ".docx", ".xlsx", ".csv"]
    keep_zero = True

    with pytest.raises(OSError):
        task_func(directory, extensions, keep_zero)

def test_task_func_with_invalid_extensions():
    directory = "path/to/directory"
    extensions = ["invalid_extension"]
    keep_zero = True

    with pytest.raises(ValueError):
        task_func(directory, extensions, keep_zero)

def test_task_func_with_keep_zero_false():
    directory = "path/to/directory"
    extensions = [".txt", ".docx", ".xlsx", ".csv"]
    keep_zero = False

    counter = task_func(directory, extensions, keep_zero)

    assert isinstance(counter, Counter)
    assert all(suffix in counter for suffix in extensions)
    assert all(counter[suffix] > 0 for suffix in extensions)