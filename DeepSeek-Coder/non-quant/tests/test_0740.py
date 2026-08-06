import pytest
from src_0740 import task_func

def test_task_func_default_key():
    result = task_func()
    assert isinstance(result, float), "The result should be a float."

def test_task_func_specific_key():
    specific_key = '470FC614'
    result = task_func(hex_key=specific_key)
    assert isinstance(result, float), "The result should be a float."
    assert result == 1.0, "The result should be 1.0 for the specific key."

def test_task_func_invalid_key():
    invalid_key = 'invalid_key'
    with pytest.raises(ValueError):
        task_func(hex_key=invalid_key)