import pytest
from src_0693 import task_func
import pandas as pd
import numpy as np

def test_task_func_with_empty_list():
    input_data = []
    expected_output = pd.DataFrame()
    assert task_func(input_data).equals(expected_output)

def test_task_func_with_single_tuple():
    input_data = [(0, np.pi/2, np.pi)]
    expected_output = pd.DataFrame({
        0: [0.0, 1.0, 0.0]
    })
    pd.testing.assert_frame_equal(task_func(input_data), expected_output)

def test_task_func_with_multiple_tuples():
    input_data = [(0, np.pi/2, np.pi), (np.pi/4, np.pi/3, np.pi/6)]
    expected_output = pd.DataFrame({
        0: [0.0, 1.0, 0.0],
        1: [np.sin(np.pi/4), np.sin(np.pi/3), np.sin(np.pi/6)]
    })
    pd.testing.assert_frame_equal(task_func(input_data), expected_output)

def test_task_func_with_negative_values():
    input_data = [(-np.pi/2, -np.pi, -np.pi/4)]
    expected_output = pd.DataFrame({
        0: [-1.0, 0.0, -np.sin(np.pi/4)]
    })
    pd.testing.assert_frame_equal(task_func(input_data), expected_output)

def test_task_func_with_non_numeric_values():
    with pytest.raises(TypeError):
        task_func([(0, 'a', np.pi)])