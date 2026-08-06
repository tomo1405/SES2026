import pytest
from src_0859 import task_func

def test_task_func():
    n = 10  # You can change this value to test different input sizes
    seed = 123  # You can change this value to test different random seeds
    result = task_func(n, seed)
    assert isinstance(result, dict)
    assert all(isinstance(key, str) and isinstance(value, int) for key, value in result.items())
    assert sum(result.values()) == n
    assert len(result) == 26