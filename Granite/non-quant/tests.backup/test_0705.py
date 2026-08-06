import pandas as pd
from itertools import combinations
from src_0705 import task_func
import pytest

# Constants
MIN_PERCENTAGE = 0.75

# Test data
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
cols = ['A', 'B', 'C']
percentage = 0.5

# Expected output
expected_output = [('A', 'B'), ('A', 'C'), ('B', 'C')]

# Test case 1: Check if the function raises a ValueError when percentage is not between 0 and 1
def test_task_func_value_error():
    with pytest.raises(ValueError):
        task_func(data, cols, -0.1)
    with pytest.raises(ValueError):
        task_func(data, cols, 1.1)

# Test case 2: Check if the function returns the correct output for the given input data
def test_task_func_correct_output():
    assert task_func(data, cols, percentage) == expected_output