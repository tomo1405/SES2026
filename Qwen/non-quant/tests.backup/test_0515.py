import pytest
from src_0515 import task_func
import pandas as pd
import matplotlib.pyplot as plt
import io
import sys

@pytest.fixture
def sample_array():
    return [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [2, 3, 4, 5, 6]
    ]

def test_task_func_returns_dataframe_and_ax(sample_array):
    df, ax = task_func(sample_array)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)

def test_task_func_dataframe_columns(sample_array):
    df, _ = task_func(sample_array)
    expected_columns = ["A", "B", "C", "D", "E"]
    assert list(df.columns) == expected_columns

def test_task_func_dataframe_values(sample_array):
    df, _ = task_func(sample_array)
    expected_sum = [8, 9, 10, 11, 12]
    assert list(df.sum()) == expected_sum

def test_task_func_plot_output(sample_array):
    # Redirect stdout to capture plot output
    captured_output = io.StringIO()
    sys.stdout = captured_output

    _, ax = task_func(sample_array)
    ax.figure.canvas.draw()

    # Reset redirect
    sys.stdout = sys.__stdout__

    # Check if any output was generated (indicating a plot was created)
    assert captured_output.getvalue() != ""