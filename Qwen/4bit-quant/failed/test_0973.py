import pytest
from src_0973 import task_func

def test_task_func_empty_path():
    assert task_func("") == []

def test_task_func_invalid_characters():
    assert task_func("<invalid:path>") == []
    assert task_func("valid/path/with|invalid") == []

def test_task_func_valid_path():
    assert task_func("/valid/path") == ["valid", "path"]
    assert task_func("C:/valid/path", "\\") == ["C:", "valid", "path"]

def test_task_func_single_component():
    assert task_func("/") == []
    assert task_func("single") == ["single"]

def test_task_func_trailing_delimiter():
    assert task_func("/valid/path/") == ["valid", "path"]
    assert task_func("C:\\valid\\path\\", "\\") == ["C:", "valid", "path"]

def test_task_func_windows_path():
    assert task_func("C:\\Windows\\System32", "\\") == ["C:", "Windows", "System32"]
    assert task_func("C:/Windows/System32") == ["C:", "Windows", "System32"]

def test_task_func_relative_path():
    assert task_func("relative/path") == ["relative", "path"]
    assert task_func("relative/path/", "/") == ["relative", "path"]

def test_task_func_root_path():
    assert task_func("/") == []
    assert task_func("\\") == []