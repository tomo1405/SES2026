import pytest
from src_0471 import task_func
import matplotlib.pyplot as plt
import numpy as np

def test_task_func():
    myList = np.random.randint(low=0, high=100, size=100)
    ax = task_func(myList)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == "Value"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Histogram of Values"