import pytest
from src_0135 import task_func
import pandas as pd
import matplotlib.pyplot as plt

# Test cases for the function
def test_task_func():
    # Test with a valid DataFrame
    data = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1]
    })
    result = task_func(data)
    assert result is not None

    # Add more test cases as needed

# Add more test cases as needed