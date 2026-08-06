import numpy as np
import bisect
import statistics
import matplotlib.pyplot as plt
from src_0199 import task_func

def test_task_func():
    data = [1, 2, 3, 4, 5]
    value = 3
    greater_avg, num_greater_value = task_func(data, value)
    assert np.array_equal(greater_avg, np.array([4, 5]))
    assert num_greater_value == 2

def test_task_func_empty_data():
    data = []
    value = 3
    greater_avg, num_greater_value = task_func(data, value)
    assert np.array_equal(greater_avg, np.array([]))
    assert num_greater_value == 0