python
import pandas as pd
import numpy as np
import pytest

from src_0865 import task_func

def test_task_func():
    # Test case 1: Empty input
    fruit_data = []
    expected_output = pd.DataFrame()
    assert task_func(fruit_data).equals(expected_output)

    # Test case 2: Single fruit input
    fruit_data = [('apple', 5)]
    expected_output = pd.DataFrame({'Total Count': [5], 'Average Count': [5]}, index=['apple'])
    assert task_func(fruit_data).equals(expected_output)

    # Test case 3: Multiple fruit input
    fruit_data = [('apple', 5), ('banana', 3), ('orange', 7)]
    expected_output = pd.DataFrame({'Total Count': [5, 3, 7], 'Average Count': [5, 3, 7]}, index=['apple', 'banana', 'orange'])
    assert task_func(fruit_data).equals(expected_output)

    # Test case 4: Duplicate fruit input
    fruit_data = [('apple', 5), ('banana', 3), ('orange', 7), ('apple', 2)]
    expected_output = pd.DataFrame({'Total Count': [5, 3, 7, 2], 'Average Count': [5, 3, 7, 2]}, index=['apple', 'banana', 'orange'])
    assert task_func(fruit_data).equals(expected_output)

    # Test case 5: Zero count input
    fruit_data = [('apple', 0), ('banana', 3), ('orange', 7)]
    expected_output = pd.DataFrame({'Total Count': [0, 3, 7], 'Average Count': [0, 3, 7]}, index=['apple', 'banana', 'orange'])
    assert task_func(fruit_data).equals(expected_output)