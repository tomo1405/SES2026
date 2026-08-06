import numpy as np
import seaborn as sns
import pytest
from src_0440 import task_func

def test_task_func():
    P = np.random.rand(10, 10)
    T = np.random.rand(10, 10)
    expected_result_shape = (10, 10)
    expected_heatmap_axes = ['x', 'y']

    result, heatmap = task_func(P, T)

    assert result.shape == expected_result_shape, "Expected result shape does not match"
    assert heatmap.get_axes().get_xlabel() == expected_heatmap_axes[0], "Expected x-axis label does not match"
    assert heatmap.get_axes().get_ylabel() == expected_heatmap_axes[1], "Expected y-axis label does not match"