import numpy as np
from itertools import zip_longest
from src_0024 import task_func

def test_task_func():
    l1 = [1, 2, 3, 4, 5]
    l2 = [1, 2, 3, 4, 5]
    THRESHOLD = 0.5
    combined = [val for pair in zip_longest(l1, l2) for val in pair if val is not None]
    differences = np.abs(np.array(combined) - THRESHOLD)
    closest_index = np.argmin(differences)
    expected_output = combined[closest_index]
    actual_output = task_func(l1, l2, THRESHOLD)
    assert actual_output == expected_output

def test_task_func_with_different_inputs():
    l1 = [1, 2, 3, 4, 5]
    l2 = [6, 7, 8, 9, 10]
    THRESHOLD = 0.5
    combined = [val for pair in zip_longest(l1, l2) for val in pair if val is not None]
    differences = np.abs(np.array(combined) - THRESHOLD)
    closest_index = np.argmin(differences)
    expected_output = combined[closest_index]
    actual_output = task_func(l1, l2, THRESHOLD)
    assert actual_output == expected_output

def test_task_func_with_negative_threshold():
    l1 = [1, 2, 3, 4, 5]
    l2 = [1, 2, 3, 4, 5]
    THRESHOLD = -0.5
    combined = [val for pair in zip_longest(l1, l2) for val in pair if val is not None]
    differences = np.abs(np.array(combined) - THRESHOLD)
    closest_index = np.argmin(differences)
    expected_output = combined[closest_index]
    actual_output = task_func(l1, l2, THRESHOLD)
    assert actual_output == expected_output