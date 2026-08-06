import pytest
from src_0902 import task_func

def test_task_func_empty_input():
    input_data = []
    expected_output = pd.DataFrame(columns=['x', 'y', 'z'])
    assert task_func(input_data).equals(expected_output)

def test_task_func_single_row():
    input_data = [[1, 2, 3]]
    expected_output = pd.DataFrame([[1, 2, 3]], columns=['x', 'y', 'z'])
    assert task_func(input_data).equals(expected_output)

def test_task_func_multiple_rows():
    input_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_output = pd.DataFrame([[0.0, 0.0, 0.0], [0.5, 0.5, 0.5], [1.0, 1.0, 1.0]], columns=['x', 'y', 'z'])
    assert task_func(input_data).equals(expected_output)

def test_task_func_with_zero_values():
    input_data = [[0, 0, 0], [0, 0, 0]]
    expected_output = pd.DataFrame([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], columns=['x', 'y', 'z'])
    assert task_func(input_data).equals(expected_output)

def test_task_func_with_negative_values():
    input_data = [[-1, -2, -3], [-4, -5, -6]]
    expected_output = pd.DataFrame([[0.0, 0.0, 0.0], [1.0, 1.0, 1.0]], columns=['x', 'y', 'z'])
    assert task_func(input_data).equals(expected_output)