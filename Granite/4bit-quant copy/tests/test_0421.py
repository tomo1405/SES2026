import pytest
from src_0421 import task_func
import pandas as pd
from sklearn.preprocessing import StandardScaler

@pytest.fixture
def input_data():
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def test_task_func(input_data):
    expected_output = [[-1.22474487, -1.22474487, -1.22474487],
                       [ 1.22474487,  1.22474487,  1.22474487],
                       [-0.47434165, -0.47434165, -0.47434165]]
    output = task_func(input_data)
    assert output.values.tolist() == expected_output

def test_task_func_with_non_numeric_data(input_data):
    input_data = [[1, 2, 'a'], [4, 5, 6], [7, 8, 9]]
    with pytest.raises(ValueError):
        task_func(input_data)