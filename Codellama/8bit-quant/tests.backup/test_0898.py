import pytest
from src_0898 import task_func

def test_task_func():
    # Test with default seed
    frequencies, ax = task_func(1000)
    assert len(frequencies) == 6
    assert all(frequency >= 0 for frequency in frequencies)
    assert ax.get_title() == 'Histogram of Dice Rolls'
    assert ax.get_xlabel() == 'Dice Value'
    assert ax.get_ylabel() == 'Frequency'

    # Test with custom seed
    frequencies, ax = task_func(1000, seed=42)
    assert len(frequencies) == 6
    assert all(frequency >= 0 for frequency in frequencies)
    assert ax.get_title() == 'Histogram of Dice Rolls'
    assert ax.get_xlabel() == 'Dice Value'
    assert ax.get_ylabel() == 'Frequency'

    # Test with invalid input
    with pytest.raises(ValueError):
        task_func(0)