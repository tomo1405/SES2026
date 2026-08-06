import pytest
from src_0754 import task_func


def test_task_func():
    # Test with n=1
    result = task_func(1)
    assert isinstance(result, float)
    assert 0 <= result <= RADIUS

    # Test with n=10
    result = task_func(10)
    assert isinstance(result, float)
    assert 0 <= result <= RADIUS

    # Test with n=100
    result = task_func(100)
    assert isinstance(result, float)
    assert 0 <= result <= RADIUS

    # Test with n=1000
    result = task_func(1000)
    assert isinstance(result, float)
    assert 0 <= result <= RADIUS

    # Test with n=0 (edge case)
    result = task_func(0)
    assert result == 0.0

    # Test with n=-1 (edge case)
    with pytest.raises(ValueError):
        task_func(-1)