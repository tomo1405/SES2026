import pytest
from src_0715 import task_func
from pathlib import Path
import sys

def test_task_func_default_path():
    # Test with default PATH_TO_APPEND
    result = task_func()
    assert result == '/path/to/whatever'
    assert Path('/path/to/whatever').exists()
    assert '/path/to/whatever' in sys.path

def test_task_func_custom_path():
    # Test with a custom path
    custom_path = '/tmp/custom/path'
    result = task_func(custom_path)
    assert result == custom_path
    assert Path(custom_path).exists()
    assert custom_path in sys.path

def test_task_func_idempotency():
    # Test that calling the function multiple times with the same path does not add duplicates to sys.path
    task_func()
    initial_sys_path_length = len(sys.path)
    task_func()
    assert len(sys.path) == initial_sys_path_length + 1  # Only one additional entry should be added

def test_task_func_nonexistent_parent():
    # Test with a path that has a nonexistent parent
    non_existent_path = '/nonexistent/parent/child'
    result = task_func(non_existent_path)
    assert result == non_existent_path
    assert Path(non_existent_path).exists()
    assert non_existent_path in sys.path

def test_task_func_relative_path():
    # Test with a relative path
    relative_path = 'relative/path'
    result = task_func(relative_path)
    assert result == Path.cwd() / relative_path
    assert Path(result).exists()
    assert str(result) in sys.path