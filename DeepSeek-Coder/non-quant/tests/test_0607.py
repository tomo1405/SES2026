import pytest
from src_0607 import task_func
import pandas as pd
import numpy as np

@pytest.fixture
def sample_matrix():
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def test_task_func(sample_matrix):
    result = task_func(sample_matrix)
    assert isinstance(result, pd.DataFrame)
    assert not result.isnull().any().any()
    assert np.allclose(result.mean(axis=0), np.zeros(3), atol=1e-10)
    assert np.allclose(result.std(axis=0), np.ones(3), atol=1e-10)