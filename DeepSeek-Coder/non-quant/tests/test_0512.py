import pytest
from src_0512 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define test cases
def test_task_func():
    # Test case 1: Basic functionality
    data = {
        "Age": [25, 30, 35],
        "Salary": [50000, 60000, 70000],
        "Experience": [3, 5, 7]
    }
    result, _ = task_func("Salary", data)
    assert result == {
        "sum": 180000,
        "mean": 60000.0,
        "min": 50000,
        "max": 70000
    }

    # Test case 2: Empty data
    data = {}
    result, _ = task_func("Salary", data)
    assert result == {
        "sum": 0,
        "mean": np.nan,
        "min": np.nan,
        "max": np.nan
    }

    # Test case 3: Check plotting
    data = {
        "Age": [25, 30, 35],
        "Salary": [50000, 60000, 70000],
        "Experience": [3, 5, 7]
    }
    _, ax = task_func("Salary", data)
    assert ax is not None

# Run the tests
if __name__ == "__main__":
    pytest.main()