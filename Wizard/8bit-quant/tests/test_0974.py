python
import os
import shutil
import pytest

from src_0974 import task_func

def test_task_func():
    # Test valid input
    assert task_func("/home/user/documents/file.txt") == [
        ("/", {"total": 10000000000, "used": 5000000000, "free": 5000000000}),
        ("home", {"total": 10000000000, "used": 5000000000, "free": 5000000000}),
        ("user", {"total": 10000000000, "used": 5000000000, "free": 5000000000}),
        ("documents", {"total": 10000000000, "used": 5000000000, "free": 5000000000}),
        ("file.txt", {"total": 1000000000, "used": 500000000, "free": 500000000}),
    ]

    # Test invalid input
    with pytest.raises(ValueError):
        task_func("")
    with pytest.raises(ValueError):
        task_func(123)
    with pytest.raises(FileNotFoundError):
        task_func("/nonexistent/path")
    with pytest.raises(ValueError):
        task_func("/home/user/documents/../invalid")