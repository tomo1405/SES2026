import pytest
from src_0115 import task_func
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def test_task_func_valid_input():
    my_dict = {'array': np.array([1, 2, 3, 4, 5])}
    expected_output = {
        'array': np.array([1, 2, 3, 4, 5]),
        'normalized_array': np.array([0.0, 0.25, 0.5, 0.75, 1.0])
    }
    result = task_func(my_dict)
    assert result == expected_output

def test_task_func_invalid_input():
    my_dict = {'array': [1, 2, 3, 4, 5]}
    with pytest.raises(TypeError):
        task_func(my_dict)