import pytest
from src_0898 import task_func

def test_task_func():
    # Test case 1: Default parameters
    rolls = 100
    seed = None
    expected_frequencies = [15, 15, 15, 15, 15, 15]
    expected_ax_title = 'Histogram of Dice Rolls'
    expected_ax_xlabel = 'Dice Value'
    expected_ax_ylabel = 'Frequency'
    frequencies, ax = task_func(rolls, seed)
    assert frequencies == expected_frequencies
    assert ax.get_title() == expected_ax_title
    assert ax.get_xlabel() == expected_ax_xlabel
    assert ax.get_ylabel() == expected_ax_ylabel

    # Test case 2: Custom parameters
    rolls = 50
    seed = 42
    expected_frequencies = [10, 10, 10, 10, 10, 10]
    expected_ax_title = 'Histogram of Dice Rolls'
    expected_ax_xlabel = 'Dice Value'
    expected_ax_ylabel = 'Frequency'
    frequencies, ax = task_func(rolls, seed)
    assert frequencies == expected_frequencies
    assert ax.get_title() == expected_ax_title
    assert ax.get_xlabel() == expected_ax_xlabel
    assert ax.get_ylabel() == expected_ax_ylabel