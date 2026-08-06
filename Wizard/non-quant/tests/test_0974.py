python
import os
import shutil
import pytest

from src_0974 import task_func

def test_task_func():
    # Test valid input
    assert task_func("/home/user/documents/file.txt") == [
        ("/", {"total": shutil.disk_usage("/").total, "used": shutil.disk_usage("/").used, "free": shutil.disk_usage("/").free}),
        ("home", {"total": shutil.disk_usage("/home").total, "used": shutil.disk_usage("/home").used, "free": shutil.disk_usage("/home").free}),
        ("user", {"total": shutil.disk_usage("/home/user").total, "used": shutil.disk_usage("/home/user").used, "free": shutil.disk_usage("/home/user").free}),
        ("documents", {"total": shutil.disk_usage("/home/user/documents").total, "used": shutil.disk_usage("/home/user/documents").used, "free": shutil.disk_usage("/home/user/documents").free}),
        ("file.txt", {"total": shutil.disk_usage("/home/user/documents/file.txt").total, "used": shutil.disk_usage("/home/user/documents/file.txt").used, "free": shutil.disk_usage("/home/user/documents/file.txt").free}),
    ]

    # Test invalid input
    with pytest.raises(ValueError):
        task_func("")
    with pytest.raises(ValueError):
        task_func(123)
    with pytest.raises(FileNotFoundError):
        task_func("/nonexistent/path")
    with pytest.raises(ValueError):
        task_func("/home/user/documents/../file.txt")
    with pytest.raises(ValueError):
        task_func("/home/user/documents/./file.txt")