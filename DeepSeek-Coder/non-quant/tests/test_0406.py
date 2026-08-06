import pytest
from src_0406 import task_func
import random
import matplotlib.pyplot as plt

def test_task_func():
    points = 10
    y, _ = task_func(points=points)
    assert len(y) == points
    assert all(0 <= yi <= 1 for yi in y)

# Additional tests can be added to cover more edge cases if needed