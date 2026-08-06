import pytest
from src_0047 import task_func
import pandas as pd
import numpy as np

@pytest.fixture
def sample_data():
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [2, 3, 4, 5, 6]
    }
    return pd.DataFrame(data)

def test_task_func(sample_data):
    df = sample_data
    result, _ = task_func(df)
    assert isinstance(result, pd.DataFrame)
    assert not result.isnull().any().any()
    assert len(result.columns) == 3

def test_plotting(sample_data):
    df = sample_data
    _, axes = task_func(df)
    assert len(axes) == df.shape[1]
    assert all(ax.get_title() for ax in axes)