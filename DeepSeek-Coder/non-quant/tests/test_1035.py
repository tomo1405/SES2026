import pytest
from src_1035 import task_func
import pandas as pd
import numpy as np

# Assuming src_1035 is the module where the function is defined

def test_task_func():
    # Test case 1: Basic test with predefined data
    s1 = pd.Series([250, 300, 150, 400, 200])
    s2 = pd.Series([220, 250, 180, 350, 210])
    expected_output = (None, 0.0)
    result = task_func(s1=s1, s2=s2)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

    # Add more test cases as needed

# You can add more test cases to cover different scenarios