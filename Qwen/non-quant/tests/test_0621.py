import pandas as pd
import pytest
from src_0621 import task_func


def test_task_func_output_type():
    input_data = [[2, 3], [4, 5]]
    result = task_func(input_data)
    assert isinstance(result, pd.DataFrame)

def test_task_func_shape():
    input_data = [[2, 3], [4, 5]]
    result = task_func(input_data)
    expected_shape = (2*3, 4*5)
    assert result.shape == expected_shape

def test_task_func_random_values():
    input_data = [[1, 1], [1, 1]]
    result = task_func(input_data)
    assert result.values.min() >= RANGE[0] and result.values.max() <= RANGE[1]

def test_task_func_empty_input():
    with pytest.raises(IndexError):
        task_func([])

def test_task_func_non_list_input():
    with pytest.raises(TypeError):
        task_func(123)

def test_task_func_negative_dimensions():
    input_data = [[-1, -1], [-1, -1]]
    with pytest.raises(ValueError):
        task_func(input_data)