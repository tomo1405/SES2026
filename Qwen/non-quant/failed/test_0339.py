import pytest
from src_0339 import task_func
from matplotlib import pyplot as plt

def test_task_func_output():
    elements = ['a', 'b', 'c']
    random_patterns, ax, char_count = task_func(elements)

    # Check that the number of random patterns matches the input elements
    assert len(random_patterns) == len(elements)

    # Check that each pattern is in the correct format
    for pattern in random_patterns:
        assert pattern.startswith('% ')
        assert pattern.endswith(' %')
        assert len(pattern[2:-2]) == 5

    # Check that the axes object is of the correct type
    assert isinstance(ax, plt.Axes)

    # Check that the character count dictionary is not empty
    assert char_count

# Additional tests can be added to further validate the function's behavior