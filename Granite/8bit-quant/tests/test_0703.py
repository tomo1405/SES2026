import pandas as pd
from sklearn.decomposition import PCA
import pytest

def task_func(df):
    pca = PCA(n_components=2)
    df_pca = pca.fit_transform(df)
    
    df_pca = pd.DataFrame(df_pca, columns=['PC1', 'PC2'])
    
    return df_pca

def test_task_func():
    # Create a sample input DataFrame for testing
    df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['A', 'B', 'C'])
    
    # Call the function and store the result
    result = task_func(df)
    
    # Define the expected output DataFrame
    expected_result = pd.DataFrame([[1.0, 0.0], [0.0, 1.0], [1.0, 0.0]], columns=['PC1', 'PC2'])
    
    # Use the assert_frame_equal function from pandas.util.testing to compare the result with the expected output
    assert pd.util.testing.assert_frame_equal(result, expected_result)
    
    # Use pytest.raises to check if the function raises an exception for invalid input
    with pytest.raises(ValueError):
        task_func('invalid input')