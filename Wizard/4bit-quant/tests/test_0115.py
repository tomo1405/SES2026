python
import numpy as np
import pytest
from src_0115 import task_func

def test_task_func():
    # Test case 1: Normal input
    my_dict = {"array": np.array([1, 2, 3, 4, 5])}
    expected_dict = {"array": np.array([1, 2, 3, 4, 5]), "normalized_array": np.array([0., 0.25, 0.5, 0.75, 1.])}
    assert task_func(my_dict) == expected_dict

    # Test case 2: Input with non-numpy array
    my_dict = {"array": [1, 2, 3, 4, 5]}
    with pytest.raises(TypeError):
        task_func(my_dict)

    # Test case 3: Input with empty array
    my_dict = {"array": np.array([])}
    with pytest.raises(ValueError):
        task_func(my_dict)