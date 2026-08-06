import pytest
from src_0962 import task_func

def test_task_func():
    directory = "path/to/directory"
    extensions = [".txt", ".docx", ".xlsx", ".csv"]
    keep_zero = True

    counter = task_func(directory, extensions, keep_zero)

    assert isinstance(counter, Counter)
    assert all(isinstance(key, str) and key.startswith(".") for key in counter.keys())
    assert all(isinstance(value, int) for value in counter.values())
    assert all(value >= 0 for value in counter.values())