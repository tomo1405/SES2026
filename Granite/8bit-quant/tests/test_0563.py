import pytest
from src_0563 import task_func

def test_task_func():
    # Test invalid filepath type
    with pytest.raises(TypeError):
        task_func(123)

    # Test invalid filepath
    with pytest.raises(OSError):
        task_func("")

    # Test valid filepath
    lib = task_func("valid_filepath.so")
    assert lib._name is not None