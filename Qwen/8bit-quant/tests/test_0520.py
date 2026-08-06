import pytest
from src_0520 import task_func
import pandas as pd
import io
import matplotlib.pyplot as plt

def test_task_func_with_valid_data():
    data = {
        'Apple': [10, 20, 30],
        'Banana': [15, 25, 35],
        'Cherry': [5, 10, 15]
    }
    fig = task_func(data)
    assert isinstance(fig, plt.Axes)

def test_task_func_with_missing_values():
    data = {
        'Apple': [10, None, 30],
        'Banana': [None, 25, 35],
        'Cherry': [5, 10, None]
    }
    fig = task_func(data)
    assert isinstance(fig, plt.Axes)

def test_task_func_with_single_column():
    data = {
        'Apple': [10, 20, 30]
    }
    fig = task_func(data)
    assert isinstance(fig, plt.Axes)

def test_task_func_with_empty_data():
    data = {}
    with pytest.raises(ValueError):
        task_func(data)

def test_task_func_with_non_numeric_data():
    data = {
        'Apple': ['a', 'b', 'c'],
        'Banana': [15, 25, 35]
    }
    with pytest.raises(TypeError):
        task_func(data)

def test_task_func_plot_labels():
    data = {
        'Apple': [10, 20, 30],
        'Banana': [15, 25, 35]
    }
    fig = task_func(data)
    assert fig.get_xlabel() == "Time"
    assert fig.get_ylabel() == "Sales Quantity"
    assert fig.get_title() == "Fruit Sales over Time"
    assert set([text.get_text() for text in fig.get_legend().get_texts()]) == {'Apple', 'Banana'}