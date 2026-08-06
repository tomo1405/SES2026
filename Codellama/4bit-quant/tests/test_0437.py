import string

import matplotlib
import pytest
from src_0437 import task_func


def test_task_func():
    # Test that the function raises a TypeError when the input is not a string
    with pytest.raises(TypeError):
        task_func(123)

    # Test that the function returns a dictionary and a matplotlib Axes object
    result = task_func("hello world")
    assert isinstance(result, tuple)
    assert isinstance(result[0], dict)
    assert isinstance(result[1], matplotlib.axes.Axes)

    # Test that the dictionary contains the correct keys and values
    letter_counts, ax = result
    assert set(letter_counts.keys()) == set(string.ascii_lowercase)
    assert all(isinstance(value, int) for value in letter_counts.values())

    # Test that the Axes object has the correct labels and title
    assert ax.get_xlabel() == "Letters"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Letter Frequencies"

    # Test that the Axes object has the correct bar plot
    assert ax.get_xlim() == (0, 26)
    assert ax.get_ylim() == (0, 12)
    assert ax.get_xticks() == np.arange(26)
    assert ax.get_yticks() == np.arange(12)