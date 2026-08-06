import pytest
from src_1022 import task_func

def test_task_func_valid_input():
    result = task_func("test_string")
    assert result == "a94a8fe5ccb19ba61c4c0873d391e987982fbbd3"

def test_task_func_with_verify_hash():
    result = task_func("test_string", "expected_hash")
    assert result is True

def test_task_func_invalid_input_type():
    with pytest.raises(TypeError):
        task_func(12345)

def test_task_func_invalid_verify_hash_type():
    with pytest.raises(TypeError):
        task_func("test_string", 12345)