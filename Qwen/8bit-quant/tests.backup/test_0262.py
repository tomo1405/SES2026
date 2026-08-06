import pytest
from src_0262 import task_func
import matplotlib.pyplot as plt
import numpy as np

def test_task_func_invalid_radius():
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    with pytest.raises(ValueError, match='Radius must be non-negative'):
        task_func(ax, -1)

def test_task_func_invalid_ax_type():
    fig, ax = plt.subplots()
    with pytest.raises(TypeError, match='ax must be a polar plot'):
        task_func(ax, 1)

def test_task_func_valid_input():
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    result = task_func(ax, 2)
    assert isinstance(result, plt.Axes)
    assert np.allclose(result.lines[0].get_ydata(), 2 * np.ones(1000))
    assert result.get_rlabel_position() == 90

def test_task_func_zero_radius():
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    result = task_func(ax, 0)
    assert isinstance(result, plt.Axes)
    assert np.allclose(result.lines[0].get_ydata(), np.zeros(1000))
    assert result.get_rlabel_position() == 0