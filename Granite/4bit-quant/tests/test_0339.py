import pytest
from src_0339 import task_func

def test_task_func():
    elements = ['apple', 'banana', 'cherry']
    seed = 100
    random_patterns, ax, char_count = task_func(elements, seed)

    assert len(random_patterns) == len(elements)
    assert ax.get_xlabel() == 'Character'
    assert ax.get_ylabel() == 'Count'
    assert all(isinstance(key, str) for key in char_count.keys())
    assert all(isinstance(value, int) for value in char_count.values())