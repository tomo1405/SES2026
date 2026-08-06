import pytest
from src_0370 import task_func

def test_task_func():
    # Test case 1: Test with a list of numbers
    l1 = [1, 2, 3, 4, 5]
    ax1 = task_func(l1)
    assert ax1 is not None  # Check if the returned ax object is not None

    # Test case 2: Test with a list of strings
    l2 = ['a', 'b', 'c', 'd', 'e']
    ax2 = task_func(l2)
    assert ax2 is not None  # Check if the returned ax object is not None

    # Test case 3: Test with a list of mixed types
    l3 = [1, 'a', 2.5, 'b', 3]
    ax3 = task_func(l3)
    assert ax3 is not None  # Check if the returned ax object is not None