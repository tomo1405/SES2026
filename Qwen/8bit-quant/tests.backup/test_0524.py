import pytest
from src_0524 import task_func
import pandas as pd
import matplotlib.pyplot as plt
import io
import sys

def test_task_func_empty_data():
    assert task_func([]) is None

def test_task_func_single_column():
    data = {'A': [1, 2, 3]}
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == "Time"
    assert ax.get_ylabel() == "Data Points"
    assert ax.get_title() == "Data over Time"
    lines = ax.get_lines()
    assert len(lines) == 1
    assert lines[0].get_label() == 'A'

def test_task_func_multiple_columns():
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == "Time"
    assert ax.get_ylabel() == "Data Points"
    assert ax.get_title() == "Data over Time"
    lines = ax.get_lines()
    assert len(lines) == 2
    labels = [line.get_label() for line in lines]
    assert set(labels) == {'A', 'B'}

def test_task_func_plot_output():
    data = {'A': [1, 2, 3]}
    captured_output = io.StringIO()
    sys.stdout = captured_output
    task_func(data)
    sys.stdout = sys.__stdout__
    # Since we are capturing stdout, we can't directly check the plot output.
    # However, we can ensure that no errors were raised during the plotting process.
    assert "Traceback" not in captured_output.getvalue()