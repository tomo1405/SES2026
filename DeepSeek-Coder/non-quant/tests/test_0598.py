import pytest
from src_0598 import task_func
import pandas as pd
import time

# Define test cases
def test_task_func():
    # Test case 1: Basic functionality
    data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Alice']}
    letter = 'a'
    expected_output = pd.Series(['Alice', 'Alice'], name='Name')
    assert task_func(data, letter) == expected_output

    # Add more test cases as needed

# Run the tests
if __name__ == "__main__":
    pytest.main()