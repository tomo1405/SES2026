import pytest
from src_0697 import task_func
import numpy as np
import math

def test_task_func():
    # Test case 1: radius = 1, num_points = 1
    expected_output = [(1, 0)]
    assert task_func(1, 1) == expected_output

    # Test case 2: radius = 1, num_points = 2
    expected_output = [(1, 0), (0, 1)]
    assert task_func(1, 2) == expected_output

    # Test case 3: radius = 2, num_points = 3
    expected_output = [(2, 0), (0, 2), (1, 1)]
    assert task_func(2, 3) == expected_output

    # Test case 4: radius = 3, num_points = 4
    expected_output = [(3, 0), (0, 3), (1, 2), (2, 1)]
    assert task_func(3, 4) == expected_output

    # Test case 5: radius = 4, num_points = 5
    expected_output = [(4, 0), (0, 4), (1, 3), (2, 2), (3, 1)]
    assert task_func(4, 5) == expected_output