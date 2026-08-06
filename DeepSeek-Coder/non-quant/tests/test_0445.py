import pytest
from src_0445 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Test with default parameters
    points, _ = task_func()
    assert points.shape == (100, 3)

    # Add more assertions as needed to cover different scenarios