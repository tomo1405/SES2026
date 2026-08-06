import pytest
from src_0974 import task_func


def test_task_func_valid_path():
    path = "/path/to/directory"
    results = task_func(path)
    assert results == [
        ("path", {"total": 1000, "used": 500, "free": 500}),
        ("to", {"total": 1000, "used": 500, "free": 500}),
        ("directory", {"total": 1000, "used": 500, "free": 500}),
    ]


def test_task_func_invalid_path():
    path = ""
    with pytest.raises(ValueError):
        task_func(path)


def test_task_func_non_existent_path():
    path = "/path/to/non_existent_directory"
    with pytest.raises(FileNotFoundError):
        task_func(path)


def test_task_func_invalid_delimiter():
    path = "/path/to/directory"
    delimiter = ""
    with pytest.raises(ValueError):
        task_func(path, delimiter)