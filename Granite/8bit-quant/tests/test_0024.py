import numpy as np
from itertools import zip_longest
from src_0024 import task_func

def test_task_func():
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    THRESHOLD = 0.5
    combined = [val for pair in zip_longest(l1, l2) for val in pair if val is not None]
    differences = np.abs(np.array(combined) - THRESHOLD)
    closest_index = np.argmin(differences)
    expected_result = combined[closest_index]
    actual_result = task_func(l1, l2, THRESHOLD)
    assert actual_result == expected_result

def test_task_func_with_empty_lists():
    l1 = []
    l2 = []
    THRESHOLD = 0.5
    combined = [val for pair in zip_longest(l1, l2) for val in pair if val is not None]
    differences = np.abs(np.array(combined) - THRESHOLD)
    closest_index = np.argmin(differences)
    expected_result = combined[closest_index]
    actual_result = task_func(l1, l2, THRESHOLD)
    assert actual_result == expected_result

def test_task_func_with_threshold_zero():
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    THRESHOLD = 0
    combined = [val for pair in zip_longest(l1, l2) for val in pair if val is not None]
    differences = np.abs(np.array(combined) - THRESHOLD)
    closest_index = np.argmin(differences)
    expected_result = combined[closest_index]
    actual_result = task_func(l1, l2, THRESHOLD)
    assert actual_result == expected_result