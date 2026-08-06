import matplotlib.pyplot as plt
import numpy as np
import pytest

from src_0468 import task_func

def test_task_func():
    # Test case 1: Default parameters
    fig, points = task_func(n=10)
    assert isinstance(fig, plt.Figure)
    assert isinstance(points, list)
    assert len(points) == 10
    for x, y in points:
        assert 0 <= x < 1
        assert 0 <= y < 1

    # Test case 2: Custom parameters
    fig, points = task_func(n=5, seed=42)
    assert isinstance(fig, plt.Figure)
    assert isinstance(points, list)
    assert len(points) == 5
    for x, y in points:
        assert 0 <= x < 1
        assert 0 <= y < 1