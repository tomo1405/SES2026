import pytest
from src_0518 import task_func
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

def test_task_func():
    # Test case 1: Basic test with a simple array
    array = [[1, 2], [3, 4], [5, 6]]
    expected_df = pd.DataFrame(array)
    expected_transformed = np.array([[-0.97295548, -2.29355949], [-2.29355949, -0.97295548], [-3.6141635, 0.34764851]])
    
    df, transformed_data = task_func(array)
    
    assert np.allclose(df, expected_df).all(), "DataFrame comparison failed"
    assert np.allclose(transformed_data, expected_transformed), "Transformed data comparison failed"

    # Add more test cases as needed

# Run the test
if __name__ == "__main__":
    pytest.main()