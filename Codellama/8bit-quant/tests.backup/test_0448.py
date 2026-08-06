import pytest
from src_0448 import task_func
import numpy as np

def test_task_func():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    n_components = 2
    random_state = 42

    result = task_func(data, n_components, random_state)

    assert isinstance(result, dict)
    assert "transformed_data" in result
    assert "ax" in result
    assert isinstance(result["transformed_data"], np.ndarray)
    assert isinstance(result["ax"], plt.Axes)

    transformed_data = result["transformed_data"]
    ax = result["ax"]

    assert transformed_data.shape[1] == n_components
    assert transformed_data.shape[0] == data.shape[0]
    assert ax.shape[0] == n_components
    assert ax.shape[1] == data.shape[0]

    assert np.allclose(transformed_data, np.array([[1, 2], [3, 4], [5, 6]]))
    assert np.allclose(ax.scatter(transformed_data[:, 0], transformed_data[:, 1]), np.array([[1, 2], [3, 4], [5, 6]]))