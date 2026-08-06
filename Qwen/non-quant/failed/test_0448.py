import pytest
from src_0448 import task_func
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    return np.array([[1, 2], [3, 4], [5, 6]])

def test_task_func_default_n_components(sample_data):
    result = task_func(sample_data)
    assert isinstance(result, dict)
    assert "transformed_data" in result
    assert "ax" in result
    assert result["transformed_data"].shape == (3, 2)
    assert isinstance(result["ax"], plt.Axes)

def test_task_func_one_component(sample_data):
    result = task_func(sample_data, n_components=1)
    assert result["transformed_data"].shape == (3, 1)
    assert isinstance(result["ax"], plt.Axes)

def test_task_func_random_state(sample_data):
    result1 = task_func(sample_data, random_state=42)
    result2 = task_func(sample_data, random_state=42)
    assert np.array_equal(result1["transformed_data"], result2["transformed_data"])

def test_task_func_invalid_n_components(sample_data):
    with pytest.raises(ValueError):
        task_func(sample_data, n_components=3)

def test_task_func_zero_components(sample_data):
    with pytest.raises(ValueError):
        task_func(sample_data, n_components=0)

def test_task_func_negative_components(sample_data):
    with pytest.raises(ValueError):
        task_func(sample_data, n_components=-1)