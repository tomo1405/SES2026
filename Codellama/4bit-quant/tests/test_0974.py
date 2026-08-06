import pytest
from src_0974 import task_func

def test_task_func():
    # Test with valid path
    path = "/path/to/directory"
    results = task_func(path)
    assert results == [
        ("path", {"total": 1000, "used": 500, "free": 500}),
        ("to", {"total": 500, "used": 250, "free": 250}),
        ("directory", {"total": 250, "used": 125, "free": 125}),
    ]

    # Test with invalid path
    path = ""
    with pytest.raises(ValueError):
        task_func(path)

    # Test with non-existent path
    path = "/path/to/non-existent/directory"
    with pytest.raises(FileNotFoundError):
        task_func(path)

    # Test with invalid path components
    path = "/path/to/invalid/directory"
    with pytest.raises(ValueError):
        task_func(path)