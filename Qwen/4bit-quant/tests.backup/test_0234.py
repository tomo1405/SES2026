import pytest
from src_0234 import task_func, Object
import random
import matplotlib.pyplot as plt
import io
import base64

def test_task_func_with_random_values():
    # Create a list of Object instances with random values
    obj_list = [Object() for _ in range(100)]
    attr = 'value'
    num_bins = 30
    seed = 0

    # Call the function
    ax = task_func(obj_list, attr, num_bins, seed)

    # Check if the plot was created correctly
    assert isinstance(ax, plt.Axes)

def test_task_func_with_custom_values():
    # Create a list of Object instances with custom values
    obj_list = [Object(value=i) for i in range(10)]
    attr = 'value'
    num_bins = 30
    seed = 0

    # Call the function
    ax = task_func(obj_list, attr, num_bins, seed)

    # Check if the plot was created correctly
    assert isinstance(ax, plt.Axes)

def test_task_func_with_different_seed():
    # Create a list of Object instances with random values
    obj_list = [Object() for _ in range(100)]
    attr = 'value'
    num_bins = 30
    seed1 = 0
    seed2 = 1

    # Call the function with different seeds
    ax1 = task_func(obj_list, attr, num_bins, seed1)
    ax2 = task_func(obj_list, attr, num_bins, seed2)

    # Check if the plots are different
    buf1 = io.BytesIO()
    ax1.figure.savefig(buf1, format='png')
    buf1.seek(0)
    img1 = base64.b64encode(buf1.getvalue()).decode('utf-8')

    buf2 = io.BytesIO()
    ax2.figure.savefig(buf2, format='png')
    buf2.seek(0)
    img2 = base64.b64encode(buf2.getvalue()).decode('utf-8')

    assert img1 != img2

def test_task_func_with_invalid_attribute():
    # Create a list of Object instances with random values
    obj_list = [Object() for _ in range(100)]
    attr = 'non_existent_attr'
    num_bins = 30
    seed = 0

    with pytest.raises(AttributeError):
        task_func(obj_list, attr, num_bins, seed)