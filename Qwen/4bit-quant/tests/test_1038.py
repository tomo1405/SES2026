import pytest
from src_1038 import task_func
import pandas as pd
import numpy as np

@pytest.fixture
def sample_series():
    data1 = pd.Series(np.random.rand(100), name='feature1')
    data2 = pd.Series(np.random.rand(100), name='feature2')
    return data1, data2

def test_task_func_with_valid_input(sample_series):
    s1, s2 = sample_series
    labels, ax = task_func(s1, s2)
    assert isinstance(labels, np.ndarray)
    assert len(labels) == len(s1)
    assert ax is not None

def test_task_func_with_invalid_series_type():
    with pytest.raises(ValueError, match="s1 and s2 must be pandas Series"):
        task_func([1, 2, 3], pd.Series([1, 2, 3]))

def test_task_func_with_series_of_different_length():
    with pytest.raises(ValueError, match="s1 and s2 must have the same length"):
        task_func(pd.Series([1, 2]), pd.Series([1, 2, 3]))

def test_task_func_with_custom_n_clusters(sample_series):
    s1, s2 = sample_series
    labels, ax = task_func(s1, s2, n_clusters=5)
    assert isinstance(labels, np.ndarray)
    assert len(labels) == len(s1)
    assert ax is not None