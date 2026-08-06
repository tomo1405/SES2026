python
import pytest
from src_0875 import task_func

def test_task_func():
    points = [(0, 0), (1, 1), (2, 2)]
    expected_distances = [1.4142135623730951, 1.4142135623730951, 1.4142135623730951]
    distances = task_func(points)
    assert distances == expected_distances