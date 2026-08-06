import pytest
from src_0448 import task_func

def test_task_func():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    n_components = 2
    random_state = 42
    expected_output = {"transformed_data": np.array([[1.0, 0.0], [0.0, 1.0], [1.0, -1.0]]), "ax": None}
    actual_output = task_func(data, n_components, random_state)
    assert actual_output == expected_output

def test_task_func_with_one_dimensional_data():
    data = np.array([[1], [2], [3]])
    n_components = 1
    random_state = 42
    expected_output = {"transformed_data": np.array([[1.0], [0.0], [-1.0]]), "ax": None}
    actual_output = task_func(data, n_components, random_state)
    assert actual_output == expected_output