import pytest
from src_0524 import task_func
import pandas as pd
import matplotlib.pyplot as plt
import io
import sys

def test_task_func_empty_data():
    result = task_func([])
    assert result is None

def test_task_func_single_column():
    data = {'A': [1, 2, 3]}
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 1
    assert ax.get_xlabel() == "Time"
    assert ax.get_ylabel() == "Data Points"
    assert ax.get_title() == "Data over Time"

def test_task_func_multiple_columns():
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 2
    assert ax.get_xlabel() == "Time"
    assert ax.get_ylabel() == "Data Points"
    assert ax.get_title() == "Data over Time"

def test_task_func_plot_output():
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    ax = task_func(data)
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    assert buf.getvalue() != b''

def test_task_func_no_data():
    result = task_func(None)
    assert result is None

def test_task_func_invalid_data_type():
    with pytest.raises(TypeError):
        task_func("not a list or dict")

def test_task_func_dataframe_input():
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 2
    assert ax.get_xlabel() == "Time"
    assert ax.get_ylabel() == "Data Points"
    assert ax.get_title() == "Data over Time"