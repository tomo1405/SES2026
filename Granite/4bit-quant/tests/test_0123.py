import pytest
import numpy as np
import random

from src_0123 import task_func

def test_task_func():
    my_list = [1, 2, 3]
    random_number = random.randint(0, 100)
    expected_list = my_list + [random_number]
    expected_size = sum(expected_list)
    expected_random_array = np.random.rand(expected_size)

    result_list, result_random_array = task_func(my_list)

    assert result_list == expected_list
    assert np.array_equal(result_random_array, expected_random_array)