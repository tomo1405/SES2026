import pytest
from src_0339 import task_func
from matplotlib.figure import Figure
from collections import Counter

def test_task_func():
    elements = ['a', 'b', 'c']
    random_patterns, ax, char_count = task_func(elements)

    # Check that the number of random patterns is equal to the number of input elements
    assert len(random_patterns) == len(elements)

    # Check that each random pattern is a string of length 7 (5 random characters + 2 '%' symbols)
    for pattern in random_patterns:
        assert isinstance(pattern, str)
        assert len(pattern) == 7
        assert pattern.startswith('%') and pattern.endswith('%')
        assert all(c.isalnum() for c in pattern[1:-1])

    # Check that the axes object is a matplotlib AxesSubplot instance
    assert isinstance(ax, plt.Axes)

    # Check that the character count dictionary is not empty
    assert char_count

    # Check that the character count dictionary contains only alphanumeric characters as keys
    assert all(c.isalnum() for c in char_count.keys())

    # Check that the sum of values in the character count dictionary is equal to the total number of characters in all patterns
    total_chars = sum(len(pattern) for pattern in random_patterns)
    assert sum(char_count.values()) == total_chars

    # Check that the character count dictionary matches the expected count based on the patterns
    expected_char_count = Counter(char for pattern in random_patterns for char in pattern)
    assert char_count == expected_char_count

    # Check that the histogram plot is correctly created
    assert isinstance(ax.get_figure(), Figure)
    assert len(ax.patches) == len(char_count)

# Run the tests
if __name__ == "__main__":
    pytest.main()