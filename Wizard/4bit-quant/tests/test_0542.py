python
import pytest
from src_0542 import task_func

def test_task_func():
    # Test case 1: package_name is not a string
    with pytest.raises(TypeError):
        task_func(123)

    # Test case 2: package_name is not installed
    with pytest.raises(ImportError):
        task_func("not_installed_package")

    # Test case 3: package_name is installed
    package_name = "numpy"
    added_modules = task_func(package_name)
    assert len(added_modules) > 0
    assert all(isinstance(module_name, str) for module_name in added_modules)
    assert all(isinstance(module_path, str) for module_path in sys.path)
    assert all(module_path.startswith(package_name) for module_path in sys.path)
    assert all(module_name.startswith(package_name) for module_name in added_modules)
    assert all(module_name in sys.modules for module_name in added_modules)