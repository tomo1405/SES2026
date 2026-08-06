python
import numpy as np
import random
import pytest

def task_func(my_list):
    random_number = random.randint(0, 100)
    my_list.append(random_number)

    size = sum(my_list)
    random_array = np.random.rand(size)

    return random_array

def test_task_func():
    my_list = [1, 2, 3]
    random_array = task_func(my_list)
    assert isinstance(random_array, np.ndarray)
    assert random_array.shape == (6,)