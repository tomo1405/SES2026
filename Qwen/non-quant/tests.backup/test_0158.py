import pytest
from src_0158 import task_func
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    return np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

def test_task_func_input_type(sample_data):
    with pytest.raises(ValueError):
        task_func([1, 2, 3])  # Not a 2D array
    with pytest.raises(ValueError):
        task_func(np.array([1, 2, 3]))  # 1D array
    with pytest.raises(ValueError):
        task_func(np.array([[1, 2, 3], [4, 5]]))  # Irregular 2D array

def test_task_func_output_type(sample_data):
    df, ax = task_func(sample_data)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)

def test_task_func_correlation_matrix(sample_data):
    df, _ = task_func(sample_data)
    correlation = df.corr()
    expected_corr = pd.DataFrame({
        0: [1.0, 1.0, 1.0],
        1: [1.0, 1.0, 1.0],
        2: [1.0, 1.0, 1.0]
    })
    pd.testing.assert_frame_equal(correlation, expected_corr)

def test_task_func_average_column(sample_data):
    df, _ = task_func(sample_data)
    expected_average = pd.Series([2.0, 5.0, 8.0], name='Average')
    pd.testing.assert_series_equal(df['Average'], expected_average)

def test_task_func_plot(sample_data):
    _, ax = task_func(sample_data)
    assert isinstance(ax, plt.Axes)
    plt.close(ax.figure)  # Close the plot to prevent it from showing during tests