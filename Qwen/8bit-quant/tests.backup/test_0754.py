import pytest
from src_0754 import task_func
import math
import random
import statistics

def test_task_func():
    # Test with n=1
    result = task_func(1)
    assert isinstance(result, float)

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

    # Test with n=1 (single point at origin)
    with pytest.raises(AssertionError):
        task_func(1)  # This should fail because the distance calculation will be incorrect

    # Test with n=1 (single point on the circle)
    with pytest.raises(AssertionError):
        task_func(1)  # This should fail because the distance calculation will be incorrect

    # Test with n=1 (single point inside the circle)
    with pytest.raises(AssertionError):
        task_func(1)  # This should fail because the distance calculation will be incorrect

    # Test with n=1 (single point outside the circle)
    with pytest.raises(AssertionError):
        task_func(1)  # This should fail because the distance calculation will be incorrect