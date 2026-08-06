import pytest
from src_0968 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def test_task_func():
    def test_func(x):
        return x**2

    fig, ax = task_func(test_func)
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 2
    assert ax.get_title() == "Simple Plot"

    # Add more assertions as needed to cover different aspects of the function