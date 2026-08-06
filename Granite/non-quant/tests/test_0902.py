import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from src_0902 import task_func
import pytest

def test_task_func():
    # Test case 1: Empty input list
    input_list = []
    expected_output = pd.DataFrame(columns=['x', 'y', 'z'])
    actual_output = task_func(input_list)
    assert actual_output.equals(expected_output)

    # Test case 2: Non-empty input list
    input_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_output = pd.DataFrame(MinMaxScaler().fit_transform(input_list), columns=['x', 'y', 'z'])
    actual_output = task_func(input_list)
    assert actual_output.equals(expected_output)