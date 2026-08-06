import pytest
from src_0339 import task_func

def test_task_func():
    elements = ['a', 'b', 'c']
    seed = 100
    random_patterns, ax, char_count = task_func(elements, seed)

    assert len(random_patterns) == len(elements)
    assert all(isinstance(pattern, str) for pattern in random_patterns)
    assert all(len(pattern) == 5 for pattern in random_patterns)
    assert all(char in string.ascii_letters + string.digits for pattern in random_patterns for char in pattern)

    assert isinstance(ax, matplotlib.axes.Axes)
    assert isinstance(char_count, dict)
    assert all(isinstance(key, str) and isinstance(value, int) for key, value in char_count.items())

    # Check that the histogram plot is correct
    _, ax = plt.subplots()
    ax.bar(char_count.keys(), char_count.values())
    assert ax.get_xlabel() == 'Character'
    assert ax.get_ylabel() == 'Count'
    assert ax.get_title() == 'Histogram of Character Occurrences'
    assert ax.get_xlim() == (0, 1)
    assert ax.get_ylim() == (0, 1)
    assert ax.get_xticks() == [0, 0.2, 0.4, 0.6, 0.8, 1]
    assert ax.get_yticks() == [0, 0.2, 0.4, 0.6, 0.8, 1]
    assert ax.get_xticklabels() == ['a', 'b', 'c', 'd', 'e', 'f']
    assert ax.get_yticklabels() == ['0', '0.2', '0.4', '0.6', '0.8', '1']