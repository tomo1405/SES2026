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
    directory = "path/to/empty/directory"
    stats = task_func(directory)

    assert isinstance(stats, dict)
    assert len(stats) == len(PREFIXES)
    for prefix in PREFIXES:
        assert prefix in stats
        assert isinstance(stats[prefix], int)
        assert stats[prefix] == 0

def test_task_func_with_no_json_files():
    directory = "path/to/directory/without/json/files"
    stats = task_func(directory)

    assert isinstance(stats, dict)
    assert len(stats) == len(PREFIXES)
    for prefix in PREFIXES:
        assert prefix in stats
        assert isinstance(stats[prefix], int)
        assert stats[prefix] == 0

def test_task_func_with_invalid_directory():
    directory = "path/to/invalid/directory"
    with pytest.raises(FileNotFoundError):
        task_func(directory)