python
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import pytest

def task_func(array, seed=None):
    if seed is not None:
        np.random.seed(seed)

    if not isinstance(array, np.ndarray) or len(array.shape) != 2:
        raise ValueError("Input must be a 2D numpy array.")

    if array.size == 0 or array.shape[1] == 0:
        return pd.DataFrame(columns=["PC1", "PC2"])

    shuffled_array = np.copy(array)
    np.random.shuffle(np.transpose(shuffled_array))

    n_components = min(2, shuffled_array.shape[1])
    pca = PCA(n_components=n_components)
    principal_components = pca.fit_transform(shuffled_array)

    column_labels = ["PC1", "PC2"][:n_components]
    df = pd.DataFrame(data=principal_components, columns=column_labels)

    return df

def test_task_func():
    # Test case 1: Valid input, seed is None
    array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    expected_df = pd.DataFrame(data=[[-0.52237134, -0.85065081], [0.78801075, -0.20412415], [-0.34011596, 0.4253254]], columns=["PC1", "PC2"])
    assert task_func(array) == expected_df

    # Test case 2: Valid input, seed is not None
    array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    expected_df = pd.DataFrame(data=[[-0.52237134, -0.85065081], [0.78801075, -0.20412415], [-0.34011596, 0.4253254]], columns=["PC1", "PC2"])
    assert task_func(array, seed=42) == expected_df

    # Test case 3: Invalid input, not a 2D numpy array
    array = np.array([1, 2, 3])
    with pytest.raises(ValueError):
        task_func(array)

    # Test case 4: Invalid input, empty array
    array = np.array([])
    expected_df = pd.DataFrame(columns=["PC1", "PC2"])
    assert task_func(array) == expected_df

    # Test case 5: Invalid input, array with 0 columns
    array = np.array([[1], [2], [3]])
    expected_df = pd.DataFrame(columns=["PC1", "PC2"])
    assert task_func(array) == expected_df