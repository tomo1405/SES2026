import pytest
from src_0524 import task_func
import pandas as pd
import matplotlib.pyplot as plt
import io

def test_task_func_with_empty_data():
    result = task_func(None)
    assert result is None

def test_task_func_with_valid_data():
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    }
    fig = task_func(data)
    assert isinstance(fig, plt.Axes)

def test_task_func_with_single_column_data():
    data = {
        'A': [1, 2, 3]
    }
    fig = task_func(data)
    assert isinstance(fig, plt.Axes)

def test_task_func_plot_output():
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    }
    fig = task_func(data)
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    assert buf.getvalue() != b''

def test_task_func_labels_and_title():
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    }
    task_func(data)
    assert plt.gca().get_xlabel() == "Time"
    assert plt.gca().get_ylabel() == "Data Points"
    assert plt.gca().get_title() == "Data over Time"