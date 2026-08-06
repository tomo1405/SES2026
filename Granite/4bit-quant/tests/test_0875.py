import pytest
from src_0875 import task_func
from itertools import zip_longest
from scipy.spatial import distance

def test_task_func():
    points = [(0, 0), (1, 1), (2, 2)]
    expected_distances = [distance.euclidean((0, 0), (1, 1)), distance.euclidean((1, 1), (2, 2))]
    
    distances = task_func(points)
    
    assert distances == expected_distances

def test_task_func_with_empty_list():
    points = []
    expected_distances = []
    
    distances = task_func(points)
    
    assert distances == expected_distances

def test_task_func_with_one_point():
    points = [(0, 0)]
    expected_distances = []
    
    distances = task_func(points)
    
    assert distances == expected_distances