import pytest
from src_0739 import task_func
import numpy as np
from scipy.stats import iqr

def test_task_func():
    # Test case 1: List of integers
    L = [1, 2, 3, 4, 5]
    expected_output = iqr(L)
    actual_output = task_func(L)
    assert actual_output == expected_output, "Test case 1 failed"

    # Test case 2: List of floats
    L = [1.1, 2.2, 3.3, 4.4, 5.5]
    expected_output = iqr(L)
    actual_output = task_func(L)
    assert actual_output == expected_output, "Test case 2 failed"

    # Test case 3: List of strings
    L = ['a', 'b', 'c', 'd', 'e']
    with pytest.raises(TypeError):
        task_func(L)

    # Test case 4: List of lists
    L = [[1, 2], [3, 4], [5, 6]]
    with pytest.raises(TypeError):
        task_func(L)