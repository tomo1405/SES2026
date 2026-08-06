import pytest
import numpy as np
import matplotlib.pyplot as plt
import math
from src_0400 import task_func

def test_task_func_valid_input():
    frequency = 1.0
    sample_size = 10000
    fig, ax = task_func(frequency, sample_size)
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 2
    assert ax.lines[0].get_label() == 'sin'
    assert ax.lines[1].get_label() == 'cos'

def test_task_func_invalid_frequency():
    frequency = -1.0
    sample_size = 10000
    with pytest.raises(ValueError) as excinfo:
        task_func(frequency, sample_size)
    assert "Frequency cannot be negative" in str(excinfo.value)

def test_task_func_invalid_sample_size():
    frequency = 1.0
    sample_size = 0
    with pytest.raises(ValueError) as excinfo:
        task_func(frequency, sample_size)
    assert "Sample size cannot be negative or zero" in str(excinfo.value)