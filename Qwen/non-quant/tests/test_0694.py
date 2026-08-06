import pytest
from src_0694 import task_func
import pandas as pd
from sklearn.preprocessing import StandardScaler

def test_task_func():
    # Test with simple data
    tuples_list = [(1, 2), (3, 4), (5, 6)]
    columns = ['A', 'B']
    expected_output = pd.DataFrame({
        'A': [-1.22474487, 0., 1.22474487],
        'B': [-1.22474487, 0., 1.22474487]
    })

    result = task_func(tuples_list, columns)
    pd.testing.assert_frame_equal(result, expected_output)

    # Test with different data
    tuples_list = [(10, 20), (30, 40), (50, 60)]
    columns = ['X', 'Y']
    expected_output = pd.DataFrame({
        'X': [-1.22474487, 0., 1.22474487],
        'Y': [-1.22474487, 0., 1.22474487]
    })

    result = task_func(tuples_list, columns)
    pd.testing.assert_frame_equal(result, expected_output)

    # Test with one column
    tuples_list = [(1,), (2,), (3,)]
    columns = ['Z']
    expected_output = pd.DataFrame({
        'Z': [-1.22474487, 0., 1.22474487]
    })

    result = task_func(tuples_list, columns)
    pd.testing.assert_frame_equal(result, expected_output)

    # Test with empty list
    tuples_list = []
    columns = ['A', 'B']
    expected_output = pd.DataFrame(columns=columns)

    result = task_func(tuples_list, columns)
    pd.testing.assert_frame_equal(result, expected_output)

    # Test with single row
    tuples_list = [(1, 2)]
    columns = ['A', 'B']
    expected_output = pd.DataFrame({
        'A': [0.],
        'B': [0.]
    })

    result = task_func(tuples_list, columns)
    pd.testing.assert_frame_equal(result, expected_output)