import pytest
from src_0048 import task_func
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
    result, heatmap = task_func(df)
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert isinstance(heatmap, plt.AxesSubplot), "The heatmap should be a matplotlib AxesSubplot"
    assert len(result.columns) == len(df.columns), "The number of columns should remain the same"
    assert np.all(result.isnull().sum() == 0), "There should be no missing values"