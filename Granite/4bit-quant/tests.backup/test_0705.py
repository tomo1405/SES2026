import pandas as pd
from itertools import combinations
from src_0705 import task_func
import pytest

# Constants
MIN_PERCENTAGE = 0.75

# Test case 1: valid input
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
cols = ['A', 'B', 'C']
percentage = 0.5
expected_output = [('A', 'B'), ('A', 'C'), ('B', 'C')]

output = task_func(data, cols, percentage)
assert output == expected_output, "Test case 1 failed"

# Test case 2: invalid input (percentage out of range)
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
cols = ['A', 'B', 'C']
percentage = 1.5

with pytest.raises(ValueError) as e:
    task_func(data, cols, percentage)
assert str(e.value) == "Percentage must be between 0 and 1", "Test case 2 failed"

# Test case 3: invalid input (data is not a list of lists)
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
cols = ['A', 'B', 'C']
percentage = 0.5

with pytest.raises(TypeError) as e:
    task_func(data, cols, percentage)
assert str(e.value) == "Input data must be a list of lists", "Test case 3 failed"