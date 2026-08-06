import pytest
from src_0120 import task_func

def test_task_func():
    # Mock the required imports
    import numpy as np
    import matplotlib.pyplot as plt

    # Call the function
    task_func()

    # Check if the required plots are created
    assert plt.fignum_exists(1)
    assert plt.fignum_exists(2)

    # Check if the plot title, xlabel, and ylabel are as expected
    fig = plt.figure(1)
    assert fig.axes[0].get_title() == 'y = x^2'
    assert fig.axes[0].get_xlabel() == 'x'
    assert fig.axes[0].get_ylabel() == 'y'

    # Check if the grid is displayed
    assert fig.axes[0].gridOn