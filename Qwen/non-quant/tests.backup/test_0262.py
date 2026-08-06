import pytest
from src_0262 import task_func
import matplotlib.pyplot as plt
import numpy as np

def test_task_func_radius_zero():
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    result_ax = task_func(ax, 0)
    assert np.array_equal(result_ax.lines[0].get_ydata(), np.zeros_like(np.linspace(0, 2 * np.pi, 1000)))

def test_task_func_positive_radius():
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    radius = 5
    result_ax = task_func(ax, radius)
    expected_ydata = radius * np.ones_like(np.linspace(0, 2 * np.pi, 1000))
    assert np.array_equal(result_ax.lines[0].get_ydata(), expected_ydata)

def test_task_func_negative_radius():
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    with pytest.raises(ValueError, match='Radius must be non-negative'):
        task_func(ax, -1)

def test_task_func_non_polar_axis():
    fig, ax = plt.subplots()
    with pytest.raises(TypeError, match='ax must be a polar plot'):
        task_func(ax, 5)

def test_task_func_rlabel_position():
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    radius = 3
    result_ax = task_func(ax, radius)
    assert result_ax.get_rlabel_position() == radius * 45