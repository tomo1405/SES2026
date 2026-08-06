import pytest
from src_0464 import task_func
import numpy as np
import pandas as pd

def test_task_func():
    # Test case 1: Basic functionality
    data_str = "1,2,3,4,5"
    result, _ = task_func(data_str=data_str)
    assert np.array_equal(result, np.array([1, 2, 3, 4, 5]))

    # Add more test cases as needed