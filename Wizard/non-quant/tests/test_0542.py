python
import pytest
from src_0542 import task_func

def test_task_func():
    # Test case 1: package_name is not a string
    with pytest.raises(TypeError):
        task_func(123)

    # Test case 2: package_name is not installed
    with pytest.raises(ImportError):
        task_func("non_existent_package")

    # Test case 3: package_name is installed and has no submodules
    added_modules = task_func("os")
    assert added_modules == []

    # Test case 4: package_name is installed and has submodules
    added_modules = task_func("numpy")
    assert added_modules == ["core", "fft", "linalg", "random", "testing"]