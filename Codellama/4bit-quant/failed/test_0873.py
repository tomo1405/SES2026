import pytest
from src_0873 import task_func
import numpy as np

def test_task_func():
    # Test case 1: Empty list
    data_list = []
    expected_result = []
    assert task_func(data_list) == expected_result

    # Test case 2: List with uneven tuple lengths
    data_list = [(1, 2, 3), (4, 5), (6, 7, 8, 9)]
    expected_result = [2.0, 5.0, 7.0]
    assert task_func(data_list) == expected_result

    # Test case 3: List with non-numeric values
    data_list = [(1, 2, 3), (4, 5, 'a'), (6, 7, 8)]
    expected_result = [2.0, 5.0, 7.0]
    assert task_func(data_list) == expected_result

    # Test case 4: List with empty tuples
    data_list = [(1, 2, 3), (), (6, 7, 8)]
    expected_result = [2.0, np.nan, 7.0]
    assert task_func(data_list) == expected_result

    # Test case 5: List with non-numeric values and empty tuples
    data_list = [(1, 2, 3), (4, 5, 'a'), (6, 7, 8), (), (9, 10, 11)]
    expected_result = [2.0, 5.0, 7.0, np.nan, 10.0]
    assert task_func(data_list) == expected_result