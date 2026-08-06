import pytest
from src_0040 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_1samp

@pytest.fixture
def data():
    np.random.seed(42)
    data_matrix = np.random.rand(10, 5)
    return data_matrix

def test_task_func(data):
    significant_indices, _ = task_func(data)
    assert len(significant_indices) > 0, "Expected at least one significant index"