import pytest
from src_0091 import task_func
import numpy as np
import pandas as pd

def test_task_func_invalid_k():
    data = pd.DataFrame([[52.5200, 13.4050], [48.8566, 2.3522]], columns=['latitude', 'longitude'])
    target = [51.5074, -0.1278]
    with pytest.raises(ValueError, match="'k' must be a non-negative integer"):
        task_func(data, target, -1)

def test_task_func_zero_k():
    data = pd.DataFrame([[52.5200, 13.4050], [48.8566, 2.3522]], columns=['latitude', 'longitude'])
    target = [51.5074, -0.1278]
    assert task_func(data, target, 0) == []

def test_task_func_one_nearest_neighbor():
    data = pd.DataFrame([[52.5200, 13.4050], [48.8566, 2.3522]], columns=['latitude', 'longitude'])
    target = [51.5074, -0.1278]
    nearest_neighbors = task_func(data, target, 1)
    assert len(nearest_neighbors) == 1

def test_task_func_all_nearest_neighbors():
    data = pd.DataFrame([[52.5200, 13.4050], [48.8566, 2.3522]], columns=['latitude', 'longitude'])
    target = [51.5074, -0.1278]
    nearest_neighbors = task_func(data, target, 2)
    assert len(nearest_neighbors) == 2

def test_task_func_with_identical_points():
    data = pd.DataFrame([[51.5074, -0.1278], [51.5074, -0.1278]], columns=['latitude', 'longitude'])
    target = [51.5074, -0.1278]
    nearest_neighbors = task_func(data, target, 2)
    assert nearest_neighbors == [[51.5074, -0.1278], [51.5074, -0.1278]]

def test_task_func_with_large_dataset():
    data = pd.DataFrame(np.random.rand(1000, 2) * 180 - 90, columns=['latitude', 'longitude'])
    target = [51.5074, -0.1278]
    nearest_neighbors = task_func(data, target, 5)
    assert len(nearest_neighbors) == 5