import pytest
from src_0448 import task_func
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    return np.array([[1, 2], [3, 4], [5, 6]])

def test_task_func_default_n_components(sample_data):
    result = task_func(sample_data)
    assert result["transformed_data"].shape == (3, 2)
    assert isinstance(result["ax"], plt.Axes)

def test_task_func_custom_n_components(sample_data):
    result = task_func(sample_data, n_components=1)
    assert result["transformed_data"].shape == (3, 1)
    assert isinstance(result["ax"], plt.Axes)

def test_task_func_random_state(sample_data):
    result1 = task_func(sample_data, random_state=42)
    result2 = task_func(sample_data, random_state=42)
    assert np.allclose(result1["transformed_data"], result2["transformed_data"])

def test_task_func_plot_1d(sample_data):
    result = task_func(sample_data, n_components=1)
    assert result["transformed_data"].shape == (3, 1)
    assert result["ax"].get_lines()[0].get_xdata().shape == (3,)
    assert np.all(result["ax"].get_lines()[0].get_ydata() == 0)

def test_task_func_plot_2d(sample_data):
    result = task_func(sample_data)
    assert result["transformed_data"].shape == (3, 2)
    assert result["ax"].get_lines()[0].get_xdata().shape == (3,)
    assert result["ax"].get_lines()[0].get_ydata().shape == (3,)