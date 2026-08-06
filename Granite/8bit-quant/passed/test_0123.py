import numpy as np
import random
from src_0123 import task_func

def test_task_func():
    my_list = [1, 2, 3]
    random_array = task_func(my_list)
    assert isinstance(random_array, np.ndarray)
    assert random_array.shape[0] == sum(my_list)

def test_task_func_with_empty_list():
    my_list = []
    random_array = task_func(my_list)
    assert isinstance(random_array, np.ndarray)
    assert random_array.shape[0] == 0

def test_task_func_with_negative_numbers():
    my_list = [-1, -2, -3]
    random_array = task_func(my_list)
    assert isinstance(random_array, np.ndarray)
    assert random_array.shape[0] == sum(my_list)