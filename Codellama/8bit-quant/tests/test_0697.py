import pytest
from src_0697 import task_func
import numpy as np
import math

def test_task_func():
    # Test case 1: radius = 1, num_points = 1
    expected_output = [(1, 0)]
    assert task_func(1, 1) == expected_output

    # Test case 2: radius = 1, num_points = 10
    expected_output = [(1, 0), (0.5, 0.8660254037844387), (0.5, -0.8660254037844387), (-0.5, -0.8660254037844387), (-0.5, 0.8660254037844387), (0, 1), (0.5, 0.8660254037844387), (0.5, -0.8660254037844387), (-0.5, -0.8660254037844387), (-0.5, 0.8660254037844387)]
    assert task_func(1, 10) == expected_output

    # Test case 3: radius = 2, num_points = 5
    expected_output = [(2, 0), (1.5, 1.2246467991473533), (1.5, -1.2246467991473533), (-1.5, -1.2246467991473533), (-1.5, 1.2246467991473533)]
    assert task_func(2, 5) == expected_output