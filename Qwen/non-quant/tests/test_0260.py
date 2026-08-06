import pytest
from src_0260 import task_func
import matplotlib.pyplot as plt
import numpy as np

def test_task_func_invalid_ax():
    with pytest.raises(ValueError, match="The input is not an axes"):
        task_func(None, 10)

def test_task_func_valid_ax():
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    result_ax = task_func(ax, 10)
    assert result_ax == ax

def test_task_func_num_points():
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    task_func(ax, 10)
    assert len(ax.collections) == 1
    assert ax.collections[0].get_offsets().shape == (10, 2)

def test_task_func_rlabel_position():
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    task_func(ax, 10)
    assert ax.get_rlabel_position() == 1

def test_task_func_random_data():
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    task_func(ax, 10)
    offsets = ax.collections[0].get_offsets()
    assert np.all(offsets[:, 0] >= 0) and np.all(offsets[:, 0] <= 2 * np.pi)
    assert np.all(offsets[:, 1] >= 0) and np.all(offsets[:, 1] <= 1)