import pytest
from src_0339 import task_func

def test_task_func():
    elements = ['apple', 'banana', 'cherry']
    seed = 100
    random_patterns, ax, char_count = task_func(elements, seed)
    assert isinstance(random_patterns, list)
    assert len(random_patterns) == len(elements)
    assert isinstance(ax, object)
    assert isinstance(char_count, dict)
    assert len(char_count) > 0

def test_task_func_with_invalid_input():
    with pytest.raises(TypeError):
        task_func('invalid_input', 100)
    with pytest.raises(ValueError):
        task_func(['apple', 'banana', 'cherry'], 'invalid_seed')