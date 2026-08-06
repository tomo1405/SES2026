import pytest
from src_0973 import task_func

def test_task_func_empty_path():
    assert task_func("") == []

def test_task_func_single_component():
    assert task_func("file.txt") == ["file.txt"]

def test_task_func_multiple_components():
    assert task_func("folder/subfolder/file.txt") == ["folder", "subfolder", "file.txt"]

def test_task_func_windows_path():
    assert task_func("C:\\folder\\subfolder\\file.txt") == ["C:", "folder", "subfolder", "file.txt"]

def test_task_func_invalid_characters():
    assert task_func("invalid<name>.txt") == []
    assert task_func("invalid:name.txt") == []
    assert task_func("invalid|name.txt") == []
    assert task_func("invalid?name.txt") == []
    assert task_func("invalid*name.txt") == []

def test_task_func_trailing_delimiter():
    assert task_func("folder/subfolder/") == ["folder", "subfolder"]

def test_task_func_leading_delimiter():
    assert task_func("/folder/subfolder") == ["folder", "subfolder"]

def test_task_func_double_delimiters():
    assert task_func("folder//subfolder") == ["folder", "subfolder"]

def test_task_func_root_path():
    assert task_func("/") == []

def test_task_func_single_dot():
    assert task_func(".") == []

def test_task_func_double_dots():
    assert task_func("..") == []

def test_task_func_hidden_file():
    assert task_func(".hiddenfile.txt") == [".hiddenfile.txt"]

def test_task_func_hidden_folder():
    assert task_func(".hiddenfolder/file.txt") == [".hiddenfolder", "file.txt"]