import pytest
from src_0445 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    points, ax = task_func()
    assert isinstance(points, np.ndarray)
    assert points.shape == (100, 3)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == "X"
    assert ax.get_ylabel() == "Y"
    assert ax.get_zlabel() == "Z"

def test_task_func_with_n_points():
    points, ax = task_func(n_points=50)
    assert isinstance(points, np.ndarray)
    assert points.shape == (50, 3)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == "X"
    assert ax.get_ylabel() == "Y"
    assert ax.get_zlabel() == "Z"

def test_task_func_with_random_seed():
    points, ax = task_func(random_seed=42)
    assert isinstance(points, np.ndarray)
    assert points.shape == (100, 3)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == "X"
    assert ax.get_ylabel() == "Y"
    assert ax.get_zlabel() == "Z"

def test_task_func_with_invalid_n_points():
    with pytest.raises(ValueError):
        task_func(n_points=-1)

def test_task_func_with_invalid_random_seed():
    with pytest.raises(ValueError):
        task_func(random_seed="abc")