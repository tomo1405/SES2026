import pytest
from src_0790 import task_func
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def test_task_func_output_shape():
    result = task_func()
    assert result.shape == (ARRAY_LENGTH, 1), "The output shape should be (10, 1)"

def test_task_func_output_values():
    expected_output = np.array([
        [0.13636364],
        [0.27272727],
        [0.40909091],
        [0.54545455],
        [0.68181818],
        [0.81818182],
        [0.        ],
        [0.90909091],
        [0.72727273],
        [0.36363636]
    ])
    result = task_func()
    np.testing.assert_almost_equal(result, expected_output, decimal=8, err_msg="The output values do not match the expected scaled values")

def test_task_func_reproducibility():
    first_run = task_func()
    second_run = task_func()
    np.testing.assert_array_equal(first_run, second_run, err_msg="The function does not produce the same output on consecutive runs with the same seed")