import os
import sys

import pytest
from src_0542 import task_func


def test_task_func_with_existing_package():
    # Mocking the package and its modules
    package_name = 'mock_package'
    mock_package_path = '/path/to/mock_package'
    
    # Create a mock package
    sys.modules[package_name] = type(sys)('mock_package')
    sys.modules[package_name].__path__ = [mock_package_path]
    
    # Create mock modules within the package
    mock_modules = ['module1', 'module2']
    for module in mock_modules:
        module_path = os.path.join(mock_package_path, f'{module}.py')
        with open(module_path, 'w') as f:
            f.write('')
        sys.modules[f'{package_name}.{module}'] = type(sys)(f'{package_name}.{module}')
    
    # Call the function
    result = task_func(package_name)
    
    # Check if the result contains the correct module names
    assert set(result) == set(mock_modules)
    
    # Clean up
    for module in mock_modules:
        del sys.modules[f'{package_name}.{module}']
    del sys.modules[package_name]

def test_task_func_with_nonexistent_package():
    with pytest.raises(ImportError) as excinfo:
        task_func('nonexistent_package')
    assert "The package 'nonexistent_package' is not installed! Please install the package first using 'pip install nonexistent_package'" in str(excinfo.value)

def test_task_func_with_no_modules():
    package_name = 'empty_package'
    mock_package_path = '/path/to/empty_package'
    
    # Create a mock package with no modules
    sys.modules[package_name] = type(sys)('empty_package')
    sys.modules[package_name].__path__ = [mock_package_path]
    
    # Call the function
    result = task_func(package_name)
    
    # Check if the result is empty
    assert result == []
    
    # Clean up
    del sys.modules[package_name]