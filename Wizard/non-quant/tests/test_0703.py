python
import pandas as pd
import pytest
from sklearn.decomposition import PCA
from src_0703 import task_func

def test_task_func():
    # Test case 1: Test with a dataframe with 10 rows and 3 columns
    df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24], [25, 26, 27], [28, 29, 30]], columns=['A', 'B', 'C'])
    expected_df = pd.DataFrame([[1.464, -0.139], [-0.517, -0.851], [0.346, -0.399], [-0.935, 0.357], [0.694, 0.714], [-0.259, 0.966], [0.983, 0.177], [-0.177, -0.984], [0.714, -0.694], [-0.399, 0.517]], columns=['PC1', 'PC2'])
    assert task_func(df).equals(expected_df)
    
    # Test case 2: Test with a dataframe with 5 rows and 2 columns
    df = pd.DataFrame([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]], columns=['A', 'B'])
    expected_df = pd.DataFrame([[1.464, -0.139], [-0.517, -0.851], [0.346, -0.399], [-0.935, 0.357], [0.694, 0.714]], columns=['PC1', 'PC2'])
    assert task_func(df).equals(expected_df)