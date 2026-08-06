import pytest
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from src_0583 import task_func

def test_task_func():
    fig = task_func()
    assert isinstance(fig, plt.Figure)

def test_task_func_with_size():
    size = 1000
    fig = task_func(size=size)
    assert fig.axes[0].lines[0].get_xdata().size == size

def test_task_func_with_custom_size():
    size = 500
    fig = task_func(size=size)
    assert fig.axes[0].lines[0].get_xdata().size == size

def test_task_func_with_invalid_size():
    with pytest.raises(ValueError):
        task_func(size='invalid')