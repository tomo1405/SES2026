import pytest
from src_0898 import task_func

def test_task_func():
    # Test case 1: Test with default arguments
    frequencies, ax = task_func(rolls=100)
    assert isinstance(frequencies, list) and len(frequencies) == 6
    assert ax.get_title() == 'Histogram of Dice Rolls'
    assert ax.get_xlabel() == 'Dice Value'
    assert ax.get_ylabel() == 'Frequency'

    # Test case 2: Test with custom arguments
    frequencies, ax = task_func(rolls=100, seed=42)
    assert isinstance(frequencies, list) and len(frequencies) == 6
    assert ax.get_title() == 'Histogram of Dice Rolls'
    assert ax.get_xlabel() == 'Dice Value'
    assert ax.get_ylabel() == 'Frequency'