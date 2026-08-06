import pytest
from src_0875 import task_func

def test_task_func():
    points = [(0, 0), (1, 1), (2, 2), (3, 3)]
    expected_distances = [1, 1, 1, 1]
    assert task_func(points) == expected_distances

def test_task_func_with_different_points():
    points = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
    expected_distances = [1, 1, 1, 1, 1]
    assert task_func(points) == expected_distances

def test_task_func_with_empty_list():
    points = []
    expected_distances = []
    assert task_func(points) == expected_distances

def test_task_func_with_single_point():
    points = [(0, 0)]
    expected_distances = []
    assert task_func(points) == expected_distances