import pytest
from src_0445 import task_func
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func_default():
    points, ax = task_func()
    assert isinstance(points, np.ndarray)
    assert points.shape == (100, 3)
    assert isinstance(ax, plt.Axes)

def test_task_func_custom_n_points():
    n_points = 50
    points, ax = task_func(n_points=n_points)
    assert isinstance(points, np.ndarray)
    assert points.shape == (n_points, 3)
    assert isinstance(ax, plt.Axes)

def test_task_func_random_seed():
    random_seed = 42
    points1, _ = task_func(random_seed=random_seed)
    points2, _ = task_func(random_seed=random_seed)
    assert np.array_equal(points1, points2)

def test_task_func_plot():
    _, ax = task_func()
    fig = ax.get_figure()
    buf = BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    assert len(image_base64) > 0