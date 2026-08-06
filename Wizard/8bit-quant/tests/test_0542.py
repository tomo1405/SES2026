python
import pytest
from src_0542 import task_func

def test_task_func_valid_package():
    added_modules = task_func('os')
    assert added_modules == ['os']

def test_task_func_invalid_package():
    with pytest.raises(ImportError):
        task_func('invalid_package')

def test_task_func_already_imported():
    added_modules = task_func('os')
    assert added_modules == []