import pytest
from src_0227 import task_func
import numpy as np
import math
import matplotlib.pyplot as plt

def test_task_func():
    data, ax = task_func()
    assert isinstance(data, tuple)
    assert len(data) == 2
    assert isinstance(data[0], np.ndarray)
    assert isinstance(data[1], np.ndarray)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Exponential Function Plot"
    assert ax.get_xlabel() == "x"
    assert ax.get_ylabel() == "e^x"

def test_task_func_with_args():
    data, ax = task_func(range_start=0, range_end=2, step=0.1)
    assert isinstance(data, tuple)
    assert len(data) == 2
    assert isinstance(data[0], np.ndarray)
    assert isinstance(data[1], np.ndarray)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Exponential Function Plot"
    assert ax.get_xlabel() == "x"
    assert ax.get_ylabel() == "e^x"