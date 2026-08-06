import pytest
from src_0563 import task_func

def test_task_func_invalid_filepath():
    with pytest.raises(TypeError):
        task_func(123)

def test_task_func_empty_filepath():
    with pytest.raises(OSError):
        task_func("")

def test_task_func_invalid_filepath_exists():
    with pytest.raises(OSError):
        task_func("invalid_filepath")

def test_task_func_valid_filepath():
    lib = task_func("valid_filepath")
    assert lib._name == "valid_filepath"