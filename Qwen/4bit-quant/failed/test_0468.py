import pytest
from src_0468 import task_func
import matplotlib.pyplot as plt

def test_task_func():
    # Test with n=5 and default seed=0
    fig, points = task_func(5)
    
    # Check if the figure is created
    assert isinstance(fig, plt.Figure), "The function should return a matplotlib Figure object"
    
    # Check if the points are correctly generated and returned
    expected_points = [(0.5488135039273248, 0.7151893663724195),
                       (0.6027633760716439, 0.5448831828462924),
                       (0.4236547993389047, 0.6458941136654853),
                       (0.4375872137567461, 0.8917730007820798),
                       (0.9636627605646986, 0.3834415188257343)]
    assert points == expected_points, "The generated points do not match the expected values"

    # Test with different seed
    fig, points_with_new_seed = task_func(5, seed=1)
    assert points_with_new_seed != expected_points, "Points should differ with a different seed"

    # Test with n=0
    fig, empty_points = task_func(0)
    assert empty_points == [], "Points list should be empty when n=0"

    # Test with n=1
    fig, single_point = task_func(1)
    assert len(single_point) == 1, "There should be exactly one point when n=1"