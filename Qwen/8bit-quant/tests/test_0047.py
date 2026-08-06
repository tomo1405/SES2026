import pytest
from src_0047 import task_func
import pandas as pd
import numpy as np

@pytest.fixture
def sample_df():
    data = {
        'A': [1, 2, np.nan, 4],
        'B': [5, np.nan, np.nan, 8],
        'C': [9, 10, 11, 12]
    }
    return pd.DataFrame(data)

def test_task_func(sample_df):
    df, axes = task_func(sample_df)
    
    # Check if missing values are filled with the mean of the column
    assert df['A'].mean() == pytest.approx(2.5)
    assert df['B'].mean() == pytest.approx(6.5)
    
    # Check if Z-scores are computed correctly
    expected_zscores_A = [-1.34164079, -0.4472136, 0.4472136, 1.34164079]
    expected_zscores_B = [-1.34164079, 0.4472136, 0.4472136, 1.34164079]
    expected_zscores_C = [-1.34164079, -0.4472136, 0.4472136, 1.34164079]
    
    assert df['A'].tolist() == pytest.approx(expected_zscores_A)
    assert df['B'].tolist() == pytest.approx(expected_zscores_B)
    assert df['C'].tolist() == pytest.approx(expected_zscores_C)
    
    # Check if axes are returned correctly
    assert isinstance(axes, np.ndarray)
    assert axes.shape == (1, df.shape[1])