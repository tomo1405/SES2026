import pytest
from src_0436 import task_func
import pandas as pd

def test_task_func():
    # Test case 1: Basic test with valid inputs
    result = task_func("John", 30, "A123", 50000.0, "Experienced professional")
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert result.shape == (1, 6), "The DataFrame should have the correct number of columns"

    # Add more test cases as needed

    # Add more test cases to cover different scenarios