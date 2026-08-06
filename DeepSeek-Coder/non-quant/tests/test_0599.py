import pytest
from src_0599 import task_func
import pandas as pd
import time

# Define test cases
def test_task_func():
    # Test case 1: Basic functionality
    data = {'Word': ['apple', 'banana', 'cherry', 'date']}
    df = pd.DataFrame(data)
    result = task_func(df, 'a')
    assert result == {'apple': 1, 'banana': 1, 'cherry': 1, 'date': 0}

    # Add more test cases as needed

# Run the tests
if __name__ == "__main__":
    pytest.main()