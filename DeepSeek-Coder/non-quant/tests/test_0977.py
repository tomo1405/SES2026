import pytest
from src_0977 import task_func
import numpy as np
import pandas as pd

def test_task_func():
    # Test case 1: Basic functionality
    records = np.array([[1, 2, 3], [4, 5, 6]])
    result = task_func(records=records)
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"

    # Add more assertions to cover different scenarios

    # Add more test cases as needed