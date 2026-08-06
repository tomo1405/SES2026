import pytest
from src_0448 import task_func
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    return np.array([[1, 2], [3, 4], [5, 6]])

def test_task_func_output_type(sample_data):
    result = task_func(sample_data)
    assert isinstance(result, dict)
    assert "transformed_data" in result
    assert "ax" in result

def test_task_func_transformed_data_shape(sample_data):
    result = task_func(sample_data)
    transformed_data = result["transformed_data"]
    assert isinstance(transformed_data, np.ndarray)
    assert transformed_data.shape == (3, 2)

def test_task_func_transformed_data_with_n_components(sample_data):
    result = task_func(sample_data, n_components=1)
    transformed_data = result["transformed_data"]
    assert transformed_data.shape == (3, 1)

def test_task_func_random_state(sample_data):
    result1 = task_func(sample_data, random_state=42)
    result2 = task_func(sample_data, random_state=42)
    assert np.array_equal(result1["transformed_data"], result2["transformed_data"])

def test_task_func_plotting(sample_data):
    result = task_func(sample_data)
    ax = result["ax"]
    assert isinstance(ax, plt.Axes)
    lines = ax.get_lines()
    assert len(lines) == 1
    xdata, ydata = lines[0].get_data()
    assert np.array_equal(xdata, result["transformed_data"][:, 0])
    assert np.array_equal(ydata, result["transformed_data"][:, 1])

def test_task_func_one_dimensional_data(sample_data):
    pca = PCA(n_components=1)
    transformed_data = pca.fit_transform(sample_data)
    result = task_func(sample_data, n_components=1)
    assert np.array_equal(result["transformed_data"], transformed_data)
    ax = result["ax"]
    assert isinstance(ax, plt.Axes)
    lines = ax.get_lines()
    assert len(lines) == 1
    xdata, ydata = lines[0].get_data()
    assert np.array_equal(xdata, result["transformed_data"][:, 0])
    assert np.allclose(ydata, np.zeros_like(result["transformed_data"][:, 0]))