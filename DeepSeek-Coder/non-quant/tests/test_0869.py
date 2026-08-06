import pytest
from src_0869 import task_func

def test_task_func():
    # Test with default parameters
    result = task_func(5)
    assert len(result) == 5
    assert all(isinstance(color, str) for color in result)

    # Test with specific seed
    result = task_func(3, rng_seed=42)
    assert result == ['Red', 'Green', 'Blue', 'Yellow', 'Purple']

    # Test with specific number of colors
    result = task_func(3)
    assert len(result) == 3

    # Test with specific seed
    result = task_func(2, rng_seed=123)
    assert result == ['Red', 'Green']

    print("All tests passed.")