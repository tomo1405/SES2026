import pytest
from src_0260 import task_func
import matplotlib.pyplot as plt
import numpy as np

def test_task_func_invalid_ax():
    with pytest.raises(ValueError) as excinfo:
        task_func(None, 10)
    assert str(excinfo.value) == "The input is not an axes"

def test_task_func_valid_ax():
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    result = task_func(ax, 10)
    assert isinstance(result, plt.Axes)

def test_task_func_num_points():
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    task_func(ax, 10)
    assert len(ax.collections) == 1
    assert ax.collections[0].get_offsets().shape == (10, 2)

def test_task_func_rlabel_position():
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    task_func(ax, 50)
    assert ax.get_rlabel_position() == 5

def test_task_func_no_side_effects():
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    task_func(ax, 10)
    task_func(ax, 10)
    assert len(ax.collections) == 2