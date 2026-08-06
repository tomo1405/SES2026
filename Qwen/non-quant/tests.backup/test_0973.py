import pytest
from src_0973 import task_func

def test_task_func_empty_path():
    assert task_func("") == []

def test_task_func_no_components():
    assert task_func("/") == []

def test_task_func_single_component():
    assert task_func("/home") == ["home"]

def test_task_func_multiple_components():
    assert task_func("/home/user/documents") == ["home", "user", "documents"]

def test_task_func_windows_path():
    assert task_func("C:\\Users\\User\\Documents") == ["C:", "Users", "User", "Documents"]

def test_task_func_invalid_characters():
    assert task_func("/home/user<documents>") == []

def test_task_func_invalid_characters_in_component():
    assert task_func("/home/user:documents") == []

def test_task_func_trailing_delimiter():
    assert task_func("/home/user/") == ["home", "user"]

def test_task_func_leading_delimiter():
    assert task_func("/home/user") == ["home", "user"]

def test_task_func_delimiter_only():
    assert task_func("/") == []

def test_task_func_dot_components():
    assert task_func("/home/./user/..") == ["home", "user"]

def test_task_func_hidden_files():
    assert task_func("/home/.hidden") == [".hidden"]