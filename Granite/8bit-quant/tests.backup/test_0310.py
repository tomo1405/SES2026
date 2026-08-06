import numpy as np
import random
from sklearn.preprocessing import MinMaxScaler
from src_0310 import task_func

def test_task_func():
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    scaled_data = task_func(list_of_lists)
    assert isinstance(scaled_data, list)
    for scaled_list in scaled_data:
        assert isinstance(scaled_list, list)
        assert all(isinstance(x, float) for x in scaled_list)
    expected_scaled_data = [
        [0.0, 0.25, 0.5],
        [0.0, 0.25, 0.5],
        [0.0, 0.25, 0.5]
    ]
    np.testing.assert_almost_equal(scaled_data, expected_scaled_data)

def test_task_func_with_seed():
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    seed = 42
    scaled_data_1 = task_func(list_of_lists, seed=seed)
    scaled_data_2 = task_func(list_of_lists, seed=seed)
    assert scaled_data_1 == scaled_data_2

def test_task_func_with_empty_list():
    list_of_lists = [[], [4, 5, 6], [7, 8, 9]]
    scaled_data = task_func(list_of_lists)
    assert isinstance(scaled_data, list)
    for scaled_list in scaled_data:
        assert isinstance(scaled_list, list)
        assert all(isinstance(x, float) for x in scaled_list)