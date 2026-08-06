import pytest
from src_0256 import task_func
import matplotlib.pyplot as plt
import numpy as np

def test_task_func_invalid_ax():
    with pytest.raises(ValueError) as excinfo:
        task_func("not an axes", 0)
    assert str(excinfo.value) == "The input is not an axes"

def test_task_func_valid_input():
    fig, ax = plt.subplots()
    result = task_func(ax, 0)
    assert isinstance(result, plt.Axes)

def test_task_func_plot_sine():
    fig, ax = plt.subplots()
    task_func(ax, 0)
    x = np.linspace(0, 2 * np.pi, 1000)
    y = np.sin(x)
    assert np.allclose(ax.lines[0].get_xdata(), x)
    assert np.allclose(ax.lines[0].get_ydata(), y)

def test_task_func_plot_cosine():
    fig, ax = plt.subplots()
    task_func(ax, 1)
    x = np.linspace(0, 2 * np.pi, 1000)
    y = np.cos(x)
    assert np.allclose(ax.lines[0].get_xdata(), x)
    assert np.allclose(ax.lines[0].get_ydata(), y)

def test_task_func_plot_tangent():
    fig, ax = plt.subplots()
    task_func(ax, 2)
    x = np.linspace(0, 2 * np.pi, 1000)
    y = np.tan(x)
    assert np.allclose(ax.lines[0].get_xdata(), x)
    assert np.allclose(ax.lines[0].get_ydata(), y)

def test_task_func_rlabel_position():
    fig, ax = plt.subplots()
    task_func(ax, 0)
    assert ax.get_rlabel_position() == 0
    task_func(ax, 1)
    assert ax.get_rlabel_position() == 45
    task_func(ax, 2)
    assert ax.get_rlabel_position() == 90