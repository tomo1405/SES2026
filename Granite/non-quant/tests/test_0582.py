import pytest
from src_0582 import task_func
import math
import matplotlib.pyplot as plt
import numpy as np
import random

def test_task_func():
    ax = task_func()
    assert isinstance(ax, plt.Axes)

def test_task_func_with_size():
    ax = task_func(size=100)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_frequency():
    ax = task_func(frequency=2)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_size_and_frequency():
    ax = task_func(size=50, frequency=3)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_invalid_size():
    with pytest.raises(ValueError):
        task_func(size=-100)

def test_task_func_with_invalid_frequency():
    with pytest.raises(ValueError):
        task_func(frequency=-5)