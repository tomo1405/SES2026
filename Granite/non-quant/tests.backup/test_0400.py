import pytest
import numpy as np
import matplotlib.pyplot as plt
import math
from src_0400 import task_func

def test_task_func_valid_input():
    fig, ax = task_func(1.0)
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 2
    assert ax.lines[0].get_label() == 'sin'
    assert ax.lines[1].get_label() == 'cos'

def test_task_func_invalid_frequency():
    with pytest.raises(ValueError):
        task_func(-1.0)

def test_task_func_invalid_sample_size():
    with pytest.raises(ValueError):
        task_func(1.0, 0)