import pytest
from src_0687 import task_func
import numpy as np
from sklearn.preprocessing import OneHotEncoder

def test_task_func():
    # Test case 1: Basic input
    list_of_lists = [[1, 2], [3, 4]]
    expected_output = np.array([[0, 1], [1, 0], [0, 0], [0, 1]])
    assert np.array_equal(task_func(list_of_lists), expected_output)

    # Add more test cases as needed