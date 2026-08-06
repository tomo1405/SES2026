import pytest
import math
import matplotlib.pyplot as plt
import numpy as np
import random
# Constants
RANGE = 10000
SIZE = 1000
PI = np.pi
def task_func(size=SIZE, frequency=1):
    x_values = np.arange(0, size)
    y_values = [math.sin((2 * PI / RANGE) * (x + int(RANGE * random.random()) * frequency)) for x in range(size)]
    
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values)
    
    return ax
def test_task_func():
    ax = task_func()
    assert isinstance(ax, plt.Axes)
    assert ax.has_data()
def test_task_func_with_size():
    ax = task_func(size=10)
    assert isinstance(ax, plt.Axes)
    assert ax.has_data()
def test_task_func_with_frequency():
    ax = task_func(frequency=2)
    assert isinstance(ax, plt.Axes)
    assert ax.has_data()
def test_task_func_with_size_and_frequency():
    ax = task_func(size=20, frequency=2)
    assert isinstance(ax, plt.Axes)
    assert ax.has_data()