import pytest
from src_0800 import task_func
import pandas as pd
from random import seed, choices

# Test cases for task_func
def test_task_func():
    # Test case 1: Basic functionality
    L = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
    expected_output = ([], [])
    assert task_func(L) == expected_output

    # Add more test cases as needed

# Run the tests
if __name__ == "__main__":
    pytest.main()