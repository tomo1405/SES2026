import pytest
from src_1120 import task_func

def test_task_func():
    # Test case 1: Default parameters
    result = task_func()
    assert len(result) == 64
    assert result.isalnum()

    # Test case 2: Custom parameters
    password_length = 5
    salt = "sugar"
    result = task_func(password_length, salt)
    assert len(result) == 64
    assert result.isalnum()

    # Test case 3: edge cases
    with pytest.raises(ValueError):
        task_func(-1)
    with pytest.raises(TypeError):
        task_func("abc")