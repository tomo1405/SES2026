python
import pytest
from src_0875 import task_func

def test_task_func():
    points = [(0,0), (1,1), (2,2)]
    expected_distances = [1.4142135623730951, 1.4142135623730951, 1.4142135623730951]
    assert task_func(points) == expected_distances

def test_task_func_empty_points():
    points = []
    expected_distances = []
    assert task_func(points) == expected_distances

def test_task_func_one_point():
    points = [(0,0)]
    expected_distances = []
    assert task_func(points) == expected_distances

def test_task_func_two_points():
    points = [(0,0), (1,1)]
    expected_distances = [1.4142135623730951]
    assert task_func(points) == expected_distances

def test_task_func_three_points():
    points = [(0,0), (1,1), (2,2)]
    expected_distances = [1.4142135623730951, 1.4142135623730951, 1.4142135623730951]
    assert task_func(points) == expected_distances

def test_task_func_four_points():
    points = [(0,0), (1,1), (2,2), (3,3)]
    expected_distances = [1.4142135623730951, 1.4142135623730951, 1.4142135623730951, 1.7320508075688772]
    assert task_func(points) == expected_distances