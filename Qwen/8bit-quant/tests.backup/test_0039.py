import pytest
from src_0039 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    # Create a sample data matrix with random values
    return np.random.rand(10, 5)

def test_task_func_output_type(sample_data):
    df, ax = task_func(sample_data)
    assert isinstance(df, pd.DataFrame), "The first output should be a pandas DataFrame"
    assert isinstance(ax, plt.Axes), "The second output should be a matplotlib Axes object"

def test_dataframe_columns(sample_data):
    df, _ = task_func(sample_data)
    expected_columns = ["Feature 1", "Feature 2", "Feature 3", "Feature 4", "Feature 5", "Mean"]
    assert list(df.columns) == expected_columns, "DataFrame columns do not match expected columns"

def test_dataframe_shape(sample_data):
    df, _ = task_func(sample_data)
    assert df.shape == (sample_data.shape[0], len(FEATURE_NAMES) + 1), "DataFrame shape is incorrect"

def test_mean_column_values(sample_data):
    df, _ = task_func(sample_data)
    calculated_means = df.iloc[:, :-1].mean(axis=1)
    assert np.allclose(df["Mean"], calculated_means), "Mean column values do not match calculated means"

def test_plot_title(sample_data):
    _, ax = task_func(sample_data)
    assert ax.get_title() == "Distribution of Means", "Plot title is incorrect"