import pytest
from src_0400 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_valid_frequency():
    fig, ax = task_func(1)
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 2  # sin and cos lines

def test_task_func_zero_frequency():
    with pytest.raises(ValueError, match="Frequency cannot be negative"):
        task_func(-1)

def test_task_func_negative_sample_size():
    with pytest.raises(ValueError, match="Sample size cannot be negative or zero"):
        task_func(1, sample_size=-1)

def test_task_func_zero_sample_size():
    with pytest.raises(ValueError, match="Sample size cannot be negative or zero"):
        task_func(1, sample_size=0)

def test_task_func_non_default_sample_size():
    fig, ax = task_func(2, sample_size=5000)
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 2  # sin and cos lines

def test_task_func_large_frequency():
    fig, ax = task_func(10)
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 2  # sin and cos lines

def test_task_func_small_frequency():
    fig, ax = task_func(0.1)
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 2  # sin and cos lines