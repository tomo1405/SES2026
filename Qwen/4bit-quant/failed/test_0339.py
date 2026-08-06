import pytest
from src_0339 import task_func

def test_task_func():
    elements = ['a', 'b', 'c']
    random_patterns, ax, char_count = task_func(elements)

    # Check that the number of random patterns matches the number of elements
    assert len(random_patterns) == len(elements)

    # Check that each pattern is a string of length 7 (5 random characters + 2 '%')
    for pattern in random_patterns:
        assert isinstance(pattern, str)
        assert len(pattern) == 7
        assert pattern.startswith('%') and pattern.endswith('%')

    # Check that the character count dictionary is not empty
    assert char_count

    # Check that the axes object is not None
    assert ax is not None

# Additional tests can be added to check specific behavior or edge cases