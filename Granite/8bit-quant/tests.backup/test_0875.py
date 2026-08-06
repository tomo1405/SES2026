import pytest
from src_0875 import task_func
from itertools import zip_longest
from scipy.spatial import distance

def test_task_func():
    points = [(0, 0), (1, 1), (2, 2)]
    expected_distances = [distance.euclidean(points[i], points[i+1]) for i in range(len(points) - 1)]
    actual_distances = task_func(points)
    assert actual_distances == expected_distances

def test_task_func_with_empty_list():
    points = []
    expected_distances = []
    actual_distances = task_func(points)
    assert actual_distances == expected_distances

def test_task_func_with_one_point():
    points = [(0, 0)]
    expected_distances = []
    actual_distances = task_func(points)
    assert actual_distances == expected_distances

def test_task_func_with_two_points():
    points = [(0, 0), (1, 1)]
    expected_distances = [distance.euclidean(points[i], points[i+1]) for i in range(len(points) - 1)]
    actual_distances = task_func(points)
    assert actual_distances == expected_distances

def test_task_func_with_three_points():
    points = [(0, 0), (1, 1), (2, 2)]
    expected_distances = [distance.euclidean(points[i], points[i+1]) for i in range(len(points) - 1)]
    actual_distances = task_func(points)
    assert actual_distances == expected_distances