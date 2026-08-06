import math

import numpy as np
import pandas as pd
import pytest
from src_0693 import task_func


def test_task_func_with_empty_list():
    result = task_func([])
    assert result.empty

def test_task_func_with_single_tuple():
    input_data = [(0,)]
    expected_output = pd.DataFrame([[np.sin(0)]])
    result = task_func(input_data)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_with_multiple_tuples():
    input_data = [(0, math.pi), (math.pi/2, math.pi)]
    expected_output = pd.DataFrame([
        [np.sin(0), np.sin(math.pi)],
        [np.sin(math.pi/2), np.sin(math.pi)]
    ])
    result = task_func(input_data)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_with_negative_values():
    input_data = [(-math.pi/2, -math.pi)]
    expected_output = pd.DataFrame([
        [np.sin(-math.pi/2), np.sin(-math.pi)]
    ])
    result = task_func(input_data)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_with_non_numeric_values():
    with pytest.raises(TypeError):
        task_func([("a", "b")])