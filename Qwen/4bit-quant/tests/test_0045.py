import pytest
from src_0045 import task_func
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
    result_df, ax = task_func(sample_df)
    
    # Check if the DataFrame has been filled with mean values
    assert not result_df.isnull().values.any(), "DataFrame contains NaN values after filling"
    
    # Check if the scaling is applied correctly
    assert result_df.min().min() >= 0 and result_df.max().max() <= 1, "Data is not scaled between 0 and 1"
    
    # Check if the plot axis is returned
    assert ax is not None, "Plot axis is not returned"
    
    # Check if the plot is created with the correct size
    assert ax.figure.get_size_inches() == (10, 5), "Figure size is incorrect"

# Run the tests
if __name__ == "__main__":
    pytest.main()