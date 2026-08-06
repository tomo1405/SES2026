import pytest
from src_0233 import task_func
import pandas as pd
import collections

# Test cases for the function
def test_task_func():
    # Test with a valid DataFrame
    data = {
        'Customer': [1, 2, 3, 4],
        'Category': ['A', 'B', 'A', 'B'],
        'Sales': [10, 20, 30, 40]
    }
    df = pd.DataFrame(data)
    result = task_func(df=df)
    assert result == {'Total Sales': 100, 'Most Popular Category': 'A'}

    # Add more test cases as needed

# Run the tests
if __name__ == "__main__":
    pytest.main()