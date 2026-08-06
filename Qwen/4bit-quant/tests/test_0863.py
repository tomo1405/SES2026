import pytest
from src_0863 import task_func

def test_task_func_with_seed():
    seed_value = 42
    result = task_func(10, seed=seed_value)
    expected_output = {
        'a': ['a', 'a'],
        'c': ['c'],
        'd': ['d'],
        'e': ['e', 'e', 'e'],
        'g': ['g'],
        'h': ['h'],
        'i': ['i'],
        'k': ['k'],
        'l': ['l'],
        'm': ['m']
    }
    assert result == expected_output

def test_task_func_without_seed():
    result = task_func(5)
    assert isinstance(result, dict)
    for key, value in result.items():
        assert isinstance(key, str)
        assert len(key) == 1
        assert all(isinstance(item, str) and len(item) == 1 for item in value)

def test_task_func_zero_n():
    result = task_func(0)
    assert result == {}

def test_task_func_negative_n():
    with pytest.raises(ValueError):
        task_func(-1)