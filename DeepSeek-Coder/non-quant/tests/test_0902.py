import pytest
from src_0902 import task_func
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def test_empty_input():
    result = task_func([])
    expected = pd.DataFrame(columns=['x', 'y', 'z'])
    pd.testing.assert_frame_equal(result, expected)

def test_non_empty_input():
    data = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'y': 5, 'z': 6}]
    expected_df = pd.DataFrame(data)
    result = task_func(data)
    pd.testing.assert_frame_equal(result, expected_df)