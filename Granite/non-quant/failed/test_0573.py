import pytest
from src_0573 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    ax = task_func()
    assert isinstance(ax, plt.Axes)

def test_task_func_with_custom_array_length():
    ax = task_func(array_length=10)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_invalid_array_length():
    with pytest.raises(ValueError):
        task_func(array_length=-10)

def test_task_func_with_invalid_input_type():
    with pytest.raises(TypeError):
        task_func(array_length='abc')