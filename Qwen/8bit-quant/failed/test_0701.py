import pytest
from src_0701 import task_func

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

def test_task_func_with_negative_values():
    # Test with negative values
    data = [
        [-1, -2, -3],
        [-4, -5, -6],
        [-7, -8, -9]
    ]
    cols = ['A', 'B', 'C']
    expected_output = pd.DataFrame({
        'A': [1.0, 1.0, 1.0],
        'B': [1.0, 1.0, 1.0],
        'C': [1.0, 1.0, 1.0]
    }, index=['A', 'B', 'C'])
    
    result = task_func(data, cols)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_with_mixed_values():
    # Test with mixed positive and negative values
    data = [
        [1, -2, 3],
        [-4, 5, -6],
        [7, -8, 9]
    ]
    cols = ['A', 'B', 'C']
    expected_output = pd.DataFrame({
        'A': [1.0, -0.866025, 0.866025],
        'B': [-0.866025, 1.0, -0.866025],
        'C': [0.866025, -0.866025, 1.0]
    }, index=['A', 'B', 'C'])
    
    result = task_func(data, cols)
    pd.testing.assert_frame_equal(result, expected_output, check_less_precise=2)

def test_task_func_with_single_column():
    # Test with a single column
    data = [
        [1],
        [2],
        [3]
    ]
    cols = ['A']
    expected_output = pd.DataFrame({
        'A': [1.0]
    }, index=['A'])
    
    result = task_func(data, cols)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_with_empty_data():
    # Test with empty data
    data = []
    cols = ['A', 'B', 'C']
    expected_output = pd.DataFrame(columns=cols, index=cols)
    
    result = task_func(data, cols)
    pd.testing.assert_frame_equal(result, expected_output)