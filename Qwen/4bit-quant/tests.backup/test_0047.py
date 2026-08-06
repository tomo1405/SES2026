import pytest
from src_0047 import task_func
import pandas as pd
import numpy as np

@pytest.fixture
def sample_df():
    data = {
        'A': [1, 2, np.nan, 4],
        'B': [5, np.nan, 7, 8],
        'C': [9, 10, 11, 12]
    }
    return pd.DataFrame(data)

def test_task_func(sample_df):
    result_df, axes = task_func(sample_df)
    
    # Check if missing values are filled with the mean of the respective columns
    assert result_df['A'].mean() == pytest.approx(2.6666666666666665)
    assert result_df['B'].mean() == pytest.approx(6.666666666666667)
    
    # Check if the shape of the result_df is the same as the input df
    assert result_df.shape == sample_df.shape
    
    # Check if the number of axes matches the number of columns
    assert len(axes.flatten()) == sample_df.shape[1]
    
    # Check if the Z-scores are computed correctly
    z_scores = (sample_df - sample_df.mean()) / sample_df.std()
    assert result_df.equals(z_scores)