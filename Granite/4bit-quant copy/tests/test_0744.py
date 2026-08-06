import json
import os
from src_0744 import task_func
import pytest

# Constants
PREFIXES = ["is_", "has_", "can_", "should_"]

def test_task_func():
    directory = "path/to/directory"
    stats = task_func(directory)

    assert isinstance(stats, dict)
    assert len(stats) == len(PREFIXES)
    for prefix in PREFIXES:
        assert prefix in stats
        assert isinstance(stats[prefix], int)
        assert stats[prefix] >= 0

def test_task_func_with_empty_directory():
    directory = "path/to/empty_directory"
    stats = task_func(directory)

    assert isinstance(stats, dict)
    assert len(stats) == len(PREFIXES)
    for prefix in PREFIXES:
        assert prefix in stats
        assert isinstance(stats[prefix], int)
        assert stats[prefix] == 0

def test_task_func_with_nonexistent_directory():
    directory = "path/to/nonexistent_directory"
    with pytest.raises(FileNotFoundError):
        task_func(directory)