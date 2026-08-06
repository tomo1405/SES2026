python
import numpy as np
import pytest
from src_0696 import task_func

def test_task_func():
    tuples_list = [(1, 2), (3, 4), (5, 6)]
    n_components = 2

    expected_result = np.array([[ 1.22474487, -0.16222147],
                                [ 0.0707372 , -0.99749499],
                                [-1.04083402,  0.40824829]])

    result = task_func(tuples_list, n_components)

    assert np.allclose(result, expected_result)