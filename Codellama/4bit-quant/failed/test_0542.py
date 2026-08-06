import pytest
from src_0542 import task_func

def test_task_func():
    package_name = "my_package"
    added_modules = task_func(package_name)
    assert added_modules == ["module1", "module2"]

def test_task_func_with_invalid_package():
    package_name = "invalid_package"
    with pytest.raises(ImportError):
        task_func(package_name)