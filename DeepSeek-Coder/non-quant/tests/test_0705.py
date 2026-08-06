import pytest
from src_0705 import task_func
import pandas as pd
from itertools import combinations

# Constants
MIN_PERCENTAGE = 0.75

def test_task_func():
    # Test case 1: Basic functionality
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    cols = ['A', 'B', 'C']
    percentage = 0.5
    expected_output = [('A', 'B'), ('A', 'C'), ('B', 'C')]
    assert task_func(data, cols, percentage) == expected_output

    # Add more test cases as needed

if __name__ == "__main__":
    pytest.main()