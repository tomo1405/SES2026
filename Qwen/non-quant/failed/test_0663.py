import pytest
from src_0663 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_with_single_point():
    x = [[1]]
    y = [[2]]
    labels = ['A']
    
    fig = task_func(x, y, labels)
    
    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 1
    ax = fig.axes[0]
    assert len(ax.lines) == 1
    line = ax.lines[0]
    assert np.array_equal(line.get_xdata(), [0])
    assert np.array_equal(line.get_ydata(), [0])
    assert line.get_label() == 'A'

def test_task_func_with_multiple_points():
    x = [[1, 2], [3, 4]]
    y = [[5, 6], [7, 8]]
    labels = ['A', 'B']
    
    fig = task_func(x, y, labels)
    
    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 1
    ax = fig.axes[0]
    assert len(ax.lines) == 2
    
    line_a = ax.lines[0]
    assert np.array_equal(line_a.get_xdata(), [0, 0])
    assert np.array_equal(line_a.get_ydata(), [0, 0])
    assert line_a.get_label() == 'A'
    
    line_b = ax.lines[1]
    assert np.array_equal(line_b.get_xdata(), [0, 0])
    assert np.array_equal(line_b.get_ydata(), [0, 0])
    assert line_b.get_label() == 'B'

def test_task_func_with_empty_data():
    x = []
    y = []
    labels = []
    
    fig = task_func(x, y, labels)
    
    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 1
    ax = fig.axes[0]
    assert len(ax.lines) == 0

def test_task_func_with_different_lengths():
    with pytest.raises(ValueError):
        task_func([[1]], [[2], [3]], ['A'])

def test_task_func_with_non_numeric_data():
    with pytest.raises(ValueError):
        task_func([['a']], [['b']], ['A'])