import pytest
from src_0002 import task_func

def test_task_func():
    # Test case 1: length is a positive integer
    result = task_func(100)
    assert isinstance(result, dict)
    assert all(isinstance(key, str) and isinstance(value, int) for key, value in result.items())

    # Test case 2: length is a negative integer
    with pytest.raises(ValueError):
        task_func(-100)

    # Test case 3: length is not an integer
    with pytest.raises(TypeError):
        task_func('abc')