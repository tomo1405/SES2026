import pytest
from src_0046 import task_func
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [1, 3, 2, 5, 4],
        'D': [4, 3, 2, 1, 5]
    }
    return pd.DataFrame(data)

def test_task_func(sample_data):
    result, _ = task_func(sample_data)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (5, 2)
    assert list(result.columns) == ["Component 1", "Component 2"]

def test_plot(sample_data):
    _, ax = task_func(sample_data)
    assert ax is not None