import pytest
from src_0450 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    data = {
        "Feature1": np.random.randn(100),
        "Feature2": np.random.randn(100),
        "Feature3": np.random.randn(100),
        "Feature4": np.random.randn(100),
        "Feature5": np.random.randn(100),
        "OtherColumn": np.random.randn(100)
    }
    return pd.DataFrame(data)

def test_task_func_output_types(sample_data):
    standardized_data, axes_list = task_func(sample_data)
    assert isinstance(standardized_data, pd.DataFrame)
    assert isinstance(axes_list, list)

def test_task_func_columns(sample_data):
    standardized_data, _ = task_func(sample_data)
    expected_columns = ["Feature1", "Feature2", "Feature3", "Feature4", "Feature5"]
    assert all(column in standardized_data.columns for column in expected_columns)

def test_task_func_scaler(sample_data):
    standardized_data, _ = task_func(sample_data)
    mean = standardized_data.mean()
    std = standardized_data.std()
    assert np.allclose(mean, 0, atol=1e-6)
    assert np.allclose(std, 1, atol=1e-6)

def test_task_func_axes_list_length(sample_data):
    _, axes_list = task_func(sample_data)
    assert len(axes_list) == 5

def test_task_func_plot_titles(sample_data):
    _, axes_list = task_func(sample_data)
    features = ["Feature1", "Feature2", "Feature3", "Feature4", "Feature5"]
    for ax, feature in zip(axes_list, features):
        assert ax.get_title() == f"Histogram of {feature}"

# To prevent plots from showing during tests
plt.ioff()