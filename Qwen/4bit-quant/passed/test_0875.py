import pytest
from src_0875 import task_func
from scipy.spatial import distance

def test_task_func_empty_list():
    assert task_func([]) == []

def test_task_func_single_point():
    assert task_func([(0, 0)]) == []

def test_task_func_two_points():
    assert task_func([(0, 0), (3, 4)]) == [5.0]

def test_task_func_multiple_points():
    points = [(0, 0), (3, 4), (6, 8)]
    expected_distances = [5.0, 5.0]
    assert task_func(points) == expected_distances

def test_task_func_identical_points():
    points = [(1, 1), (1, 1), (1, 1)]
    expected_distances = [0.0, 0.0]
    assert task_func(points) == expected_distances

def test_task_func_negative_coordinates():
    points = [(-1, -1), (-4, -5), (-7, -9)]
    expected_distances = [5.0, 5.0]
    assert task_func(points) == expected_distances

def test_task_func_mixed_dimensions():
    points = [(0, 0), (1, 1, 1), (2, 2, 2)]
    with pytest.raises(ValueError):
        task_func(points)