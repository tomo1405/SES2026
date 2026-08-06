python
import numpy as np
import seaborn as sns
import pytest

def task_func(P, T):
    if not (isinstance(P, np.ndarray) and isinstance(T, np.ndarray)):
        raise TypeError("Expected inputs to be numpy arrays")

    result = np.tensordot(P, T, axes=[1, 0])
    # Sum along the last dimension to get a 2D matrix
    result_2D = np.sum(result, axis=-1)
    heatmap = sns.heatmap(result_2D)
    return result, heatmap

def test_task_func():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[5, 6], [7, 8]])
    result, heatmap = task_func(P, T)
    assert result.shape == (2, 2)
    assert heatmap.get_title() == "Heatmap"