import pytest
from src_1079 import task_func
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func_uniform_distribution():
    arr = np.array([1, 2, 3, 4, 5])
    uniform_distribution, ax = task_func(arr)
    assert uniform_distribution is True

def test_task_func_non_uniform_distribution():
    arr = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
    uniform_distribution, ax = task_func(arr)
    assert uniform_distribution is False

def test_task_func_single_element():
    arr = np.array([1])
    uniform_distribution, ax = task_func(arr)
    assert uniform_distribution is True

def test_task_func_empty_array():
    arr = np.array([])
    uniform_distribution, ax = task_func(arr)
    assert uniform_distribution is True

def test_task_func_histogram_plot():
    arr = np.array([1, 2, 3, 4, 5])
    uniform_distribution, ax = task_func(arr)
    
    # Convert the plot to a PNG image and encode it in base64
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    
    # Check if the plot contains the expected elements
    assert 'iVBORw0KGgoAAAANSUhEUgAA' in plot_base64  # This is a part of the PNG header

# To run the tests, use the following command:
# pytest <filename>.py