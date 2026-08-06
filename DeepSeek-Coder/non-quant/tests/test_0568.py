import pytest
from src_0568 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Test data
    data = "1-2-3-4-5"
    expected_output = None  # The function does not return a value, so we expect it to return None

    # Call the function with the test data
    result = task_func(data)

    # Assertions or checks can be added here to verify the output
    assert result == expected_output