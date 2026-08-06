import pytest
from src_0830 import task_func
import pandas as pd
from statistics import mean

# Test cases for the function
def test_task_func():
    # Test case 1: Basic functionality
    data = {'Name': ['Alice', 'Bob', 'Alice', 'Bob'], 'Score': [85, 90, 88, 92]}
    df = pd.DataFrame(data)
    expected_output = {'Alice': [('Alice', 86.5)], 'Bob': [('Bob', 91.0)]}
    assert task_func(df) == expected_output

    # Add more test cases as needed

# Run the tests
if __name__ == "__main__":
    pytest.main()