import pytest
from src_0703 import task_func
import pandas as pd
from sklearn.decomposition import PCA

def test_task_func():
    # Test case 1: Test that the function returns a DataFrame with the correct column names
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    df_pca = task_func(df)
    assert isinstance(df_pca, pd.DataFrame)
    assert df_pca.columns.tolist() == ['PC1', 'PC2']

    # Test case 2: Test that the function returns a DataFrame with the correct number of rows
    assert df_pca.shape[0] == df.shape[0]

    # Test case 3: Test that the function returns a DataFrame with the correct values
    expected_values = [[1, 2], [3, 4], [5, 6]]
    assert (df_pca.values == expected_values).all()