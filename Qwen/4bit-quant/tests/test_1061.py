import pytest
from src_1061 import task_func
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

def test_task_func_empty_df():
    df = pd.DataFrame()
    column_name = 'test_column'
    message, ax = task_func(df, column_name)
    assert message == "The DataFrame is empty or the specified column has no data."
    assert isinstance(ax, plt.Axes)

def test_task_func_column_not_in_df():
    df = pd.DataFrame({'other_column': [1, 2, 3]})
    column_name = 'test_column'
    message, ax = task_func(df, column_name)
    assert message == "The DataFrame is empty or the specified column has no data."
    assert isinstance(ax, plt.Axes)

def test_task_func_all_null_column():
    df = pd.DataFrame({'test_column': [None, None, None]})
    column_name = 'test_column'
    message, ax = task_func(df, column_name)
    assert message == "The DataFrame is empty or the specified column has no data."
    assert isinstance(ax, plt.Axes)

def test_task_func_uniform_distribution():
    df = pd.DataFrame({'test_column': [1, 1, 2, 2, 3, 3]})
    column_name = 'test_column'
    message, ax = task_func(df, column_name)
    assert message == "The distribution of values is uniform."
    assert isinstance(ax, plt.Axes)

def test_task_func_non_uniform_distribution():
    df = pd.DataFrame({'test_column': [1, 1, 2, 2, 2, 3]})
    column_name = 'test_column'
    message, ax = task_func(df, column_name)
    assert message == "The distribution of values is not uniform."
    assert isinstance(ax, plt.Axes)

def test_task_func_plot_content():
    df = pd.DataFrame({'test_column': [1, 1, 2, 2, 3, 3]})
    column_name = 'test_column'
    _, ax = task_func(df, column_name)
    buf = io.BytesIO()
    ax.figure.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    assert image_base64.startswith('iVBORw0KGgoAAAANSUhEUgAA')  # Check if it's a valid PNG base64 string