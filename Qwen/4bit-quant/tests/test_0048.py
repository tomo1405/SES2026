import pytest
from src_0048 import task_func
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
    # Call the function with the sample DataFrame
    transformed_df, heatmap = task_func(sample_df)
    
    # Check that the transformed DataFrame has no NaN values
    assert not transformed_df.isnull().values.any(), "Transformed DataFrame contains NaN values"
    
    # Check that the transformed DataFrame is standardized
    assert np.allclose(transformed_df.mean(), 0, atol=1e-6), "Mean of transformed DataFrame is not close to zero"
    assert np.allclose(transformed_df.std(), 1, atol=1e-6), "Standard deviation of transformed DataFrame is not close to one"
    
    # Check that the heatmap is not None
    assert heatmap is not None, "Heatmap is None"
    
    # Check that the heatmap is a matplotlib AxesImage object
    assert isinstance(heatmap, plt.AxesImage), "Heatmap is not a matplotlib AxesImage object"

# Run the tests
if __name__ == "__main__":
    pytest.main()