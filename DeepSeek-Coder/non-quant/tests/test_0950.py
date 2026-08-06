import pytest
from src_0950 import task_func

def test_task_func():
    # Test with default seed
    result = task_func(3, 3)
    assert result.shape == (3, 3)

    # Test with specific seed
    result = task_func(2, 2, seed=42)
    assert result.shape == (2, 2)

    # Test with different seed
    result = task_func(1, 1, seed=123)
    assert result.shape == (1, 1)