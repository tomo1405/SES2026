import pytest
from src_0042 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    return np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

def test_task_func_output(sample_data):
    df, ax = task_func(sample_data)
    assert isinstance(df, pd.DataFrame)
    assert "Skewness" in df.columns
    assert len(df) == sample_data.shape[0]
    assert ax.get_title() == "Distribution of Skewness"

def test_task_func_skewness_values(sample_data):
    df, _ = task_func(sample_data)
    expected_skewness = np.array([0.0, 0.0, 0.0])  # Assuming perfect symmetry in the sample data
    assert np.allclose(df["Skewness"].values, expected_skewness)

def test_task_func_plot(sample_data):
    _, ax = task_func(sample_data)
    assert isinstance(ax, plt.Axes)
    assert ax.has_data()  # Check if there is any data plotted