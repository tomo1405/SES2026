import pytest
from src_0156 import task_func
import pandas as pd
import numpy as np
import io
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    return np.random.rand(5, 8)

def test_task_func_returns_dataframe_and_axis(sample_data):
    df, ax = task_func(sample_data)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)

def test_dataframe_has_correct_columns(sample_data):
    df, _ = task_func(sample_data)
    assert list(df.columns) == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'Average']

def test_dataframe_average_column_is_correct(sample_data):
    df, _ = task_func(sample_data)
    expected_average = sample_data.mean(axis=1)
    assert all(np.isclose(df['Average'], expected_average))

def test_plot_y_label(sample_data):
    _, ax = task_func(sample_data)
    assert ax.get_ylabel() == 'Average'

def test_plot_saves_to_buffer(sample_data):
    buf = io.BytesIO()
    df, ax = task_func(sample_data)
    ax.figure.savefig(buf, format='png')
    buf.seek(0)
    assert len(buf.getvalue()) > 0