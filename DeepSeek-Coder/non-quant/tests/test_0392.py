import pytest
from src_0392 import task_func

def test_task_func_no_errors():
    # Test when there are no errors
    result = task_func('test_directory')
    assert result[0] == True
    assert result[1] == []

def test_task_func_with_errors():
    # Test when there are errors
    result = task_func('test_directory')
    assert result[0] == False
    assert len(result[1]) > 0