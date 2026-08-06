import pytest
from src_0175 import task_func
import pandas as pd
import numpy as np

# Test cases for the function
def test_task_func():
    # Test with a valid DataFrame
    data = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    key = 'random_col'
    min_value = 1
    max_value = 10

    result = task_func(data, key, min_value, max_value)

    # Check if the function returns a DataFrame with the new column
    assert key in result.columns
    assert len(result[key]) == len(data)

    # Check if the new column is filled with random integers within the specified range
    assert all(min_value <= x <= max_value for x in result[key])

# Add more test cases as needed