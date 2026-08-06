import pytest
from src_0339 import task_func

def test_task_func():
    elements = ['apple', 'banana', 'cherry']
    seed = 100
    random_patterns, ax, char_count = task_func(elements, seed)

    assert len(random_patterns) == len(elements)
    for pattern in random_patterns:
        assert len(pattern) == 7
        assert pattern[0] == '%'
        assert pattern[-1] == '%'
        for char in pattern[1:-1]:
            assert char.isalnum()

    assert isinstance(ax, object)
    assert isinstance(char_count, dict)
    for char, count in char_count.items():
        assert isinstance(char, str)
        assert isinstance(count, int)
        assert count > 0