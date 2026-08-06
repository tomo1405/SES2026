import pytest
from src_0693 import task_func
import pandas as pd
import numpy as np

def test_task_func_with_empty_list():
    input_data = []
    expected_output = pd.DataFrame()
    assert task_func(input_data).equals(expected_output)

def test_task_func_with_single_tuple():
    input_data = [(0, math.pi/2, math.pi)]
    expected_output = pd.DataFrame({
        0: [0, 1, 0],
        1: [0, 1, 0],
        2: [0, 1, 0]
    })
    assert task_func(input_data).equals(expected_output)

def test_task_func_with_multiple_tuples():
    input_data = [(0, math.pi/2), (math.pi, 3*math.pi/2)]
    expected_output = pd.DataFrame({
        0: [0, 1],
        1: [0, -1],
        2: [-1, 0],
        3: [-1, 0]
    })
    assert task_func(input_data).equals(expected_output)

def test_task_func_with_negative_values():
    input_data = [(-math.pi/2, -math.pi)]
    expected_output = pd.DataFrame({
        0: [-1, 0],
        1: [0, -1]
    })
    assert task_func(input_data).equals(expected_output)

def test_task_func_with_non_integer_values():
    input_data = [(0.5, 1.5, 2.5)]
    expected_output = pd.DataFrame({
        0: [np.sin(0.5), np.sin(1.5), np.sin(2.5)]
    })
    assert task_func(input_data).equals(expected_output)