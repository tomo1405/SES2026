import pytest
from src_0696 import task_func
import numpy as np
from sklearn.decomposition import PCA

def test_task_func():
    tuples_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    n_components = 2
    expected_output = np.array([[1, 2], [4, 5], [7, 8]])

    output = task_func(tuples_list, n_components)

    assert np.allclose(output, expected_output)