import pytest
from src_0697 import task_func
import numpy as np
import math

def test_task_func():
    # Test with valid input
    radius = 10
    num_points = 10
    expected_output = [(10, 0), (0, 10), (-10, 0), (0, -10)]
    assert task_func(radius, num_points) == expected_output

    # Test with invalid input
    with pytest.raises(ValueError):
        task_func(-10, 10)

    with pytest.raises(ValueError):
        task_func(10, -10)