import pytest
from src_0043 import task_func
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    return np.array([[1, 2], [3, 4], [5, 6]])

def test_task_func_output_type(sample_data):
    df, ax = task_func(sample_data)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)

def test_task_func_dataframe_columns(sample_data):
    df, _ = task_func(sample_data)
    expected_columns = ["Component 1", "Component 2", "Mean"]
    assert list(df.columns) == expected_columns

def test_task_func_dataframe_mean_column(sample_data):
    df, _ = task_func(sample_data)
    mean_values = df["Mean"].values
    expected_mean_values = np.array([1.5, 3.5, 5.5])
    assert np.allclose(mean_values, expected_mean_values)

def test_task_func_pca_cumulative_explained_variance(sample_data):
    _, ax = task_func(sample_data)
    lines = ax.get_lines()
    assert len(lines) == 1
    xdata, ydata = lines[0].get_data()
    assert np.array_equal(xdata, np.arange(1, 3))
    assert np.allclose(ydata, np.array([1.0, 1.0]))

def test_task_func_default_n_components(sample_data):
    df, _ = task_func(sample_data)
    assert df.shape[1] == 3  # 2 components + 1 mean column

def test_task_func_custom_n_components(sample_data):
    df, _ = task_func(sample_data, n_components=1)
    assert df.shape[1] == 2  # 1 component + 1 mean column