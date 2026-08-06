import pytest
from src_0262 import task_func
import matplotlib.pyplot as plt
import numpy as np

def test_task_func_positive_radius():
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    result_ax = task_func(ax, 5)
    assert isinstance(result_ax, plt.PolarAxes)

def test_task_func_zero_radius():
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    result_ax = task_func(ax, 0)
    assert isinstance(result_ax, plt.PolarAxes)

def test_task_func_negative_radius():
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    with pytest.raises(ValueError, match='Radius must be non-negative'):
        task_func(ax, -5)

def test_task_func_non_polar_axis():
    fig, ax = plt.subplots()
    with pytest.raises(TypeError, match='ax must be a polar plot'):
        task_func(ax, 5)

def test_task_func_plot_data():
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    result_ax = task_func(ax, 3)
    lines = result_ax.get_lines()
    assert len(lines) == 1
    xdata, ydata = lines[0].get_data()
    assert np.allclose(xdata, np.linspace(0, 2 * np.pi, 1000))
    assert np.allclose(ydata, 3 * np.ones_like(xdata))

def test_task_func_rlabel_position():
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    result_ax = task_func(ax, 2)
    assert result_ax.get_rlabel_position() == 90