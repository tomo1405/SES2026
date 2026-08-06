import numpy as np
import pytest
from src_0448 import task_func


def test_task_func():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    n_components = 2
    random_state = 42
    expected_output = {"transformed_data": np.array([[1, 2], [3, 4], [5, 6]]), "ax": None}
    output = task_func(data, n_components, random_state)
    assert output == expected_output

def test_task_func_with_one_dimensional_data():
    data = np.array([1, 2, 3])
    n_components = 1
    random_state = 42
    expected_output = {"transformed_data": np.array([[1], [2], [3]]), "ax": None}
    output = task_func(data, n_components, random_state)
    assert output == expected_output

def test_task_func_with_invalid_input():
    data = "invalid_input"
    n_components = 2
    random_state = 42
    with pytest.raises(TypeError):
        task_func(data, n_components, random_state)