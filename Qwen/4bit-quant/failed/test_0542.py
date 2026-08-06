import pytest
from src_0542 import task_func

def test_task_func_non_existent_package():
    with pytest.raises(ImportError) as excinfo:
        task_func("non_existent_package")
    assert "The package 'non_existent_package' is not installed! Please install the package first using 'pip install non_existent_package'" in str(excinfo.value)

def test_task_func_existing_package(monkeypatch):
    # Mocking the importlib.import_module to simulate an existing package
    mock_package = type('Package', (object,), {'__path__': ['mock_path']})()
    monkeypatch.setattr(importlib, 'import_module', lambda x: mock_package)

    # Mocking the iter_modules to simulate modules within the package
    mock_modules = [('mock_module', 'module1', None), ('mock_module', 'module2', None)]
    monkeypatch.setattr(pkgutil, 'iter_modules', lambda x: mock_modules)

    # Mocking the sys.path to avoid modifying it during the test
    original_sys_path = sys.path.copy()
    monkeypatch.setattr(sys, 'path', original_sys_path + ['mock_path'])

    added_modules = task_func("mock_package")
    assert added_modules == ['module1', 'module2']

    # Verify that sys.path was not modified
    assert sys.path == original_sys_path + ['mock_path']