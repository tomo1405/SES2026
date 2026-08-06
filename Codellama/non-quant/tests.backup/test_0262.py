import pytest
from src_0262 import task_func
import matplotlib.pyplot as plt
import numpy as np

def test_task_func_positive_radius():
    ax = plt.subplot(111, projection='polar')
    radius = 10
    task_func(ax, radius)
    assert ax.get_rlabel_position() == radius * 45

def test_task_func_negative_radius():
    ax = plt.subplot(111, projection='polar')
    radius = -10
    with pytest.raises(ValueError):
        task_func(ax, radius)

def test_task_func_non_polar_ax():
    ax = plt.subplot(111)
    radius = 10
    with pytest.raises(TypeError):
        task_func(ax, radius)