python
import numpy as np
import pytest
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def task_func(P, T, tensor_shape=(3, 3, 3)):
    if not (isinstance(P, np.ndarray) and isinstance(T, np.ndarray)):
        raise TypeError("Expected inputs to be numpy arrays")

    if not T.shape == tensor_shape:
        raise ValueError("Provided tensor does not match the specified tensor_shape.")

    result = np.tensordot(P, T, axes=[1, 1]).swapaxes(0, 1)

    # Reshape the result for PCA
    result = result.reshape(result.shape[0], -1)
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(result)

    fig, ax = plt.subplots()
    ax.scatter(pca_result[:, 0], pca_result[:, 1])
    ax.set_title("PCA Result Visualization")
    ax.set_xlabel("Principal Component 1")
    ax.set_ylabel("Principal Component 2")

    return pca_result, ax

def test_task_func():
    # Test case 1: Valid inputs
    P = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    T = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]], [[3, 6, 9], [2, 5, 8], [1, 4, 7]]])
    pca_result, ax = task_func(P, T)
    assert pca_result.shape == (3, 2)
    assert ax.get_title() == "PCA Result Visualization"
    assert ax.get_xlabel() == "Principal Component 1"
    assert ax.get_ylabel() == "Principal Component 2"

    # Test case 2: Invalid input type
    with pytest.raises(TypeError):
        task_func("P", T)

    # Test case 3: Invalid tensor shape
    T = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]], [[3, 6, 9], [2, 5, 8]]])
    with pytest.raises(ValueError):
        task_func(P, T)