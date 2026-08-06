import pytest
from src_0468 import task_func
import matplotlib.pyplot as plt
import numpy as np

def test_task_func():
    # Call the function
    fig, data = task_func(10, seed=42)

    # Check the output types
    assert isinstance(fig, plt.Figure)
    assert isinstance(data, list)
    assert all(isinstance(point, tuple) and len(point) == 2 for point in data)

    # Check the plot is displayed (optional, if running interactively)
    # plt.show()