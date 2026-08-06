import pytest
from src_1061 import task_func
import pandas as pd
import matplotlib.pyplot as plt
import io
import os

# Mocking plt.show to prevent actual plotting during tests
os.environ['MPLBACKEND'] = 'Agg'

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        'A': [1, 2, 2, 3, 3, 3],
        'B': [4, 5, 5, 6, 6, 6],
        'C': [None, None, None, None, None, None]
    })

def test_task_func_empty_df(sample_df):
    empty_df = pd.DataFrame()
    message, ax = task_func(empty_df, 'A')
    assert message == "The DataFrame is empty or the specified column has no data."
    assert isinstance(ax, plt.Axes)

def test_task_func_column_not_in_df(sample_df):
    message, ax = task_func(sample_df, 'D')
    assert message == "The DataFrame is empty or the specified column has no data."
    assert isinstance(ax, plt.Axes)

def test_task_func_all_nulls(sample_df):
    message, ax = task_func(sample_df, 'C')
    assert message == "The DataFrame is empty or the specified column has no data."
    assert isinstance(ax, plt.Axes)

def test_task_func_uniform_distribution(sample_df):
    message, ax = task_func(sample_df, 'A')
    assert message == "The distribution of values is uniform."
    assert isinstance(ax, plt.Axes)

def test_task_func_non_uniform_distribution(sample_df):
    message, ax = task_func(sample_df, 'B')
    assert message == "The distribution of values is not uniform."
    assert isinstance(ax, plt.Axes)

def test_task_func_plot_contents(sample_df):
    _, ax = task_func(sample_df, 'A')
    buf = io.BytesIO()
    ax.figure.savefig(buf, format='png')
    buf.seek(0)
    assert buf.getvalue()  # Check if the plot was created