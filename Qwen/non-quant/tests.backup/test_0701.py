import pytest
from src_0701 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    # Test with simple data
    data = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    cols = ['A', 'B', 'C']
    expected_output = pd.DataFrame({
        'A': [1.0, 1.0, 1.0],
        'B': [1.0, 1.0, 1.0],
        'C': [1.0, 1.0, 1.0]
    }, index=['A', 'B', 'C'])
    
    result = task_func(data, cols)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_with_random_data():
    # Test with random data
    np.random.seed(0)
    data = np.random.rand(4, 4)
    cols = ['X', 'Y', 'Z', 'W']
    
    result = task_func(data, cols)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (4, 4)

def test_task_func_empty_data():
    # Test with empty data
    data = []
    cols = ['A', 'B', 'C']
    expected_output = pd.DataFrame(columns=cols, index=cols).fillna(1.0)
    
    result = task_func(data, cols)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_single_column():
    # Test with single column
    data = [[1], [2], [3]]
    cols = ['A']
    expected_output = pd.DataFrame({'A': [1.0]}, index=['A'])
    
    result = task_func(data, cols)
    pd.testing.assert_frame_equal(result, expected_output)