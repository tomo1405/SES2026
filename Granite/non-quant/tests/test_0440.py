import numpy as np
import seaborn as sns
from src_0440 import task_func
import pytest

def test_task_func():
    P = np.random.rand(10, 10)
    T = np.random.rand(10, 10)
    result, heatmap = task_func(P, T)
    assert isinstance(result, np.ndarray), "Expected result to be a numpy array"
    assert isinstance(heatmap, sns.matrix.Axes), "Expected heatmap to be a seaborn heatmap"
    assert result.shape == (10, 10), "Expected result to have shape (10, 10)"
    assert heatmap.shape == (10, 10), "Expected heatmap to have shape (10, 10)"