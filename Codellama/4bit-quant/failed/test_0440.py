import pytest
from src_0440 import task_func
import numpy as np
import seaborn as sns

def test_task_func():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[5, 6], [7, 8]])
    result, heatmap = task_func(P, T)
    assert isinstance(result, np.ndarray)
    assert isinstance(heatmap, sns.heatmap)
    assert result.shape == (2, 2)
    assert heatmap.shape == (2, 2)

def test_task_func_invalid_input():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[5, 6], [7, 8]])
    with pytest.raises(TypeError):
        task_func(P, T, axes=[0, 1])