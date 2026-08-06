import pytest
from src_0269 import task_func

def test_task_func():
    n_keys = 5
    n_values = 10
    result = task_func(n_keys, n_values)
    assert isinstance(result, dict)
    assert len(result) == n_keys
    for key, value in result.items():
        assert key in LETTERS
        assert isinstance(value, list)
        assert len(value) == n_values
        assert all(isinstance(x, int) for x in value)
        assert all(x > 0 for x in value)