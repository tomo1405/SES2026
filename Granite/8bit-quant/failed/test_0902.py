import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from src_0902 import task_func
import pytest

def test_task_func_with_empty_input():
    input_list = []
    expected_output = pd.DataFrame(columns=['x', 'y', 'z'])
    actual_output = task_func(input_list)
    assert actual_output.equals(expected_output)

def test_task_func_with_non_empty_input():
    input_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_output = pd.DataFrame(MinMaxScaler().fit_transform(input_list), columns=['x', 'y', 'z'])
    actual_output = task_func(input_list)
    assert actual_output.equals(expected_output)

def test_task_func_with_input_of_different_length():
    input_list = [[1, 2], [3, 4], [5, 6, 7]]
    with pytest.raises(ValueError) as excinfo:
        task_func(input_list)
    assert "Input data must have 3 features" in str(excinfo.value)