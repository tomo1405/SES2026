import pytest
from src_1079 import task_func
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func_uniform_distribution():
    arr = np.array([1, 2, 3, 1, 2, 3])
    uniform_distribution, ax = task_func(arr)
    assert uniform_distribution is True, "The array should have a uniform distribution"
    plt.close(ax.figure)

def test_task_func_non_uniform_distribution():
    arr = np.array([1, 2, 3, 1, 1, 1])
    uniform_distribution, ax = task_func(arr)
    assert uniform_distribution is False, "The array should not have a uniform distribution"
    plt.close(ax.figure)

def test_task_func_single_element():
    arr = np.array([1, 1, 1, 1])
    uniform_distribution, ax = task_func(arr)
    assert uniform_distribution is True, "A single element array should be considered uniformly distributed"
    plt.close(ax.figure)

def test_task_func_empty_array():
    arr = np.array([])
    uniform_distribution, ax = task_func(arr)
    assert uniform_distribution is True, "An empty array should be considered uniformly distributed"
    plt.close(ax.figure)

def test_task_func_plot():
    arr = np.array([1, 2, 3, 1, 2, 3])
    uniform_distribution, ax = task_func(arr)
    buf = BytesIO()
    ax.figure.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    assert image_base64.startswith("iVBORw0KGgoAAAANSUhEUgAA"), "The plot should be correctly generated"
    plt.close(ax.figure)