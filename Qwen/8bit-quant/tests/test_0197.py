import pytest
from src_0197 import task_func
import numpy as np
from matplotlib import pyplot as plt

def test_task_func_length():
    ax, numbers = task_func(10)
    assert len(numbers) == 10

def test_task_func_range():
    ax, numbers = task_func(10, range_limit=50)
    assert all(1 <= num <= 50 for num in numbers)

def test_task_func_seed():
    ax1, numbers1 = task_func(10, seed=42)
    ax2, numbers2 = task_func(10, seed=42)
    assert numbers1 == numbers2

def test_task_func_value_error():
    with pytest.raises(ValueError):
        task_func(10, range_limit=1)

def test_task_func_sorted():
    ax, numbers = task_func(10)
    assert numbers == sorted(numbers)

def test_task_func_plot():
    ax, numbers = task_func(10)
    assert isinstance(ax, plt.Axes)