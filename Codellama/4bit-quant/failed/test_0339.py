import pytest
from src_0339 import task_func

def test_task_func():
    elements = ['a', 'b', 'c']
    seed = 100
    random_patterns, ax, char_count = task_func(elements, seed)

    # Test that the random patterns are generated correctly
    assert len(random_patterns) == len(elements)
    for pattern in random_patterns:
        assert len(pattern) == 5
        assert all(char in string.ascii_letters + string.digits for char in pattern)

    # Test that the character count is correct
    assert len(char_count) == len(set(char_count.keys()))
    for char, count in char_count.items():
        assert count == len(list(filter(lambda x: x == char, random_patterns)))

    # Test that the histogram is plotted correctly
    assert ax.get_xlabel() == 'Character'
    assert ax.get_ylabel() == 'Count'
    assert ax.get_title() == 'Histogram of Character Occurrences'
    assert len(ax.get_xticks()) == len(char_count)
    assert len(ax.get_yticks()) == len(char_count)
    for tick in ax.get_xticks():
        assert tick in char_count
    for tick in ax.get_yticks():
        assert tick in char_count.values()