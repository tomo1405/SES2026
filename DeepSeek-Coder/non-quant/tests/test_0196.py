import pytest
from src_0196 import task_func

def test_task_func_mac():
    result = task_func("http://example.com")
    assert result == 0

def test_task_func_windows():
    result = task_func("http://example.com")
    assert result == 0

def test_task_func_linux():
    result = task_func("http://example.com")
    assert result == 0