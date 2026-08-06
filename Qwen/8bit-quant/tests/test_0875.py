import pytest
from src_0875 import task_func
from scipy.spatial import distance

def test_task_func_empty_list():
    assert task_func([]) == []

def test_task_func_single_point():
    assert task_func([(0, 0)]) == []

def test_task_func_two_points():
    points = [(0, 0), (3, 4)]
    expected_distances = [5.0]
    assert task_func(points) == expected_distances

def test_task_func_three_points():
    points = [(0, 0), (3, 4), (6, 8)]
    expected_distances = [5.0, 5.0]
    assert task_func(points) == expected_distances

def test_task_func_four_points():
    points = [(0, 0), (3, 4), (6, 8), (9, 12)]
    expected_distances = [5.0, 5.0, 5.0]
    assert task_func(points) == expected_distances

def test_task_func_mixed_dimensions():
    points = [(0, 0), (3, 4, 5), (6, 8)]
    with pytest.raises(ValueError):
        task_func(points)

def test_task_func_negative_coordinates():
    points = [(-1, -1), (-4, -5)]
    expected_distances = [5.0]
    assert task_func(points) == expected_distances

def test_task_func_large_numbers():
    points = [(1e6, 1e6), (1e6 + 3, 1e6 + 4)]
    expected_distances = [5.0]
    assert task_func(points) == expected_distances