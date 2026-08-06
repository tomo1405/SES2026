import pytest
from src_0440 import task_func
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[5, 6], [7, 8]])
    return P, T

def test_task_func_types(sample_data):
    P, T = sample_data
    with pytest.raises(TypeError):
        task_func(P.tolist(), T)

def test_task_func_shape(sample_data):
    P, T = sample_data
    result, _ = task_func(P, T)
    assert result.shape == (P.shape[0], T.shape[1])

def test_task_func_result(sample_data):
    P, T = sample_data
    expected_result = np.array([[19, 22], [43, 50]])
    result, _ = task_func(P, T)
    assert np.array_equal(result, expected_result)

def test_task_func_heatmap(sample_data):
    P, T = sample_data
    _, heatmap = task_func(P, T)
    assert isinstance(heatmap, sns.axisgrid.FacetGrid)
    plt.close()  # Close the plot to prevent it from showing during tests