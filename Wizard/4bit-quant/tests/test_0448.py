python
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pytest

def task_func(data, n_components=2, random_state=None):
    pca = PCA(n_components=n_components, random_state=random_state)
    transformed_data = pca.fit_transform(data)

    fig, ax = plt.subplots()
    if transformed_data.shape[1] == 1:
        ax.scatter(transformed_data[:, 0], np.zeros_like(transformed_data[:, 0]))
    else:
        ax.scatter(transformed_data[:, 0], transformed_data[:, 1])

    return {"transformed_data": transformed_data, "ax": ax}

def test_task_func():
    data = np.random.rand(100, 5)
    result = task_func(data)
    assert isinstance(result, dict)
    assert "transformed_data" in result
    assert "ax" in result
    assert isinstance(result["transformed_data"], np.ndarray)
    assert isinstance(result["ax"], plt.Axes)
    assert result["transformed_data"].shape == (100, 2)