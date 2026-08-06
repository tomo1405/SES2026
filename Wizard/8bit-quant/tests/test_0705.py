python
import pandas as pd
import pytest
from itertools import combinations
from src_0705 import task_func

# Constants
MIN_PERCENTAGE = 0.75

# Test cases
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
cols = ['a', 'b', 'c']
percentage = 0.9

# Test case 1
def test_task_func_valid_input():
    assert task_func(data, cols, percentage) == [('a', 'b')]

# Test case 2
def test_task_func_invalid_percentage():
    with pytest.raises(ValueError):
        task_func(data, cols, 1.5)

# Test case 3
def test_task_func_invalid_data():
    with pytest.raises(ValueError):
        task_func([1, 2, 3], cols, percentage)

# Test case 4
def test_task_func_invalid_cols():
    with pytest.raises(ValueError):
        task_func(data, ['a', 'b'], percentage)