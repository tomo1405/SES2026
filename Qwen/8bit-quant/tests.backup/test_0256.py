import pytest
from src_0256 import task_func
import matplotlib.pyplot as plt
import numpy as np

def test_task_func_valid_input():
    fig, ax = plt.subplots()
    result_ax = task_func(ax, 0)
    assert isinstance(result_ax, plt.Axes)
    assert result_ax.get_rlabel_position() == 0

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(None, 0)

def test_task_func_invalid_function_index():
    fig, ax = plt.subplots()
    with pytest.raises(IndexError):
        task_func(ax, 3)

def test_task_func_cos_function():
    fig, ax = plt.subplots()
    result_ax = task_func(ax, 1)
    assert isinstance(result_ax, plt.Axes)
    assert result_ax.get_rlabel_position() == 45

def test_task_func_tan_function():
    fig, ax = plt.subplots()
    result_ax = task_func(ax, 2)
    assert isinstance(result_ax, plt.Axes)
    assert result_ax.get_rlabel_position() == 90