import numpy as np
import random
from sklearn.preprocessing import MinMaxScaler
from src_0310 import task_func

def test_task_func():
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    scaled_data = task_func(list_of_lists)
    expected_result = [[0.0, 0.5, 1.0], [0.0, 0.5, 1.0], [0.0, 0.5, 1.0]]
    assert scaled_data == expected_result

def test_task_func_with_empty_list():
    list_of_lists = [[], [4, 5, 6], [7, 8, 9]]
    scaled_data = task_func(list_of_lists)
    expected_result = [[0.42211507, 0.47609611, 0.52390389], 
                       [0.0, 0.5, 1.0], 
                       [0.17971316, 0.35942632, 0.53913947]]
    assert scaled_data == expected_result

def test_task_func_with_random_seed():
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    scaled_data_1 = task_func(list_of_lists, seed=42)
    scaled_data_2 = task_func(list_of_lists, seed=42)
    assert scaled_data_1 == scaled_data_2