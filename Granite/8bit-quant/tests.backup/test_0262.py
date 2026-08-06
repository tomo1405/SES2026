import matplotlib.pyplot as plt
import numpy as np
import pytest

from src_0262 import task_func

def test_task_func():
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    radius = 5
    ax = task_func(ax, radius)
    assert ax.get_rlabel_position() == radius * 45
    theta = np.linspace(0, 2 * np.pi, 1000)
    expected_radius = radius * np.ones_like(theta)
    assert np.array_equal(ax.lines[0].get_xdata(), theta)
    assert np.array_equal(ax.lines[0].get_ydata(), expected_radius)

def test_task_func_negative_radius():
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    radius = -5
    with pytest.raises(ValueError) as excinfo:
        task_func(ax, radius)
    assert 'Radius must be non-negative' in str(excinfo.value)

def test_task_func_invalid_ax():
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=False)
    radius = 5
    with pytest.raises(TypeError) as excinfo:
        task_func(ax, radius)
    assert 'ax must be a polar plot' in str(excinfo.value)