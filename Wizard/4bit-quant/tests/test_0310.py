python
import numpy as np
import random
from sklearn.preprocessing import MinMaxScaler
import pytest

def task_func(list_of_lists, seed=42):
    np.random.seed(seed)
    random.seed(seed)
    scaled_data = []
    scaler = MinMaxScaler(feature_range=(0, 1))
    for list_ in list_of_lists:
        if not list_:
            list_ = [random.randint(0, 100) for _ in range(5)]
        # Reshape the data to fit the scaler
        reshaped_data = np.array(list_).reshape(-1, 1)
        scaled_list = scaler.fit_transform(reshaped_data)
        # Flatten the list and append to the result
        scaled_data.append(scaled_list.flatten().tolist())
    
    return scaled_data

def test_task_func():
    # Test case 1: Empty list of lists
    list_of_lists = [[]]
    expected_result = [[0.0, 0.0, 0.0, 0.0, 0.0]]
    assert task_func(list_of_lists) == expected_result
    
    # Test case 2: List of lists with random values
    list_of_lists = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
    expected_result = [[0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0]]
    assert task_func(list_of_lists) == expected_result
    
    # Test case 3: List of lists with random values and seed
    list_of_lists = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
    expected_result = [[0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0]]
    assert task_func(list_of_lists, seed=42) == expected_result
    
    # Test case 4: List of lists with random values and seed
    list_of_lists = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
    expected_result = [[0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0]]
    assert task_func(list_of_lists, seed=10) != expected_result