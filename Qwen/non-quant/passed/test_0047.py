import pytest
from src_0047 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
    
    # Check if missing values are filled with the mean
    assert df.isnull().values.any() == False
    
    # Check if the shape of the returned DataFrame is the same as the input
    assert df.shape == sample_df.shape
    
    # Check if the returned DataFrame contains only numeric values
    assert all(np.issubdtype(dtype, np.number) for dtype in df.dtypes)
    
    # Check if the plot axes are correctly returned
    assert isinstance(axes, np.ndarray)
    assert axes.shape == (1, df.shape[1])
    
    # Check if the plot is properly displayed
    plt.show()

if __name__ == "__main__":
    pytest.main()