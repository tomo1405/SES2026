import pandas as pd
from sklearn.decomposition import PCA
def task_func(df):
    pca = PCA(n_components=2)
    df_pca = pca.fit_transform(df)
    
    df_pca = pd.DataFrame(df_pca, columns=['PC1', 'PC2'])
    
    return df_pca
import pytest

def test_task_func():
    # Test case 1: input is a pandas DataFrame with 5 rows and 3 columns
    df = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [6, 7, 8, 9, 10],
        'C': [11, 12, 13, 14, 15]
    })
    expected_output = pd.DataFrame({
        'PC1': [1.41421356, -0.70710678, 0.0, -0.70710678, 1.41421356],
        'PC2': [0.0, 0.70710678, 1.0, -0.70710678, 0.0]
    })
    actual_output = task_func(df)
    assert actual_output.equals(expected_output)

    # Test case 2: input is a pandas DataFrame with 2 rows and 2 columns
    df = pd.DataFrame({
        'X': [10, 20],
        'Y': [30, 40]
    })
    expected_output = pd.DataFrame({
        'PC1': [28.28427125, 0.0],
        'PC2': [0.0, 28.28427125]
    })
    actual_output = task_func(df)
    assert actual_output.equals(expected_output)

if __name__ == "__main__":
    pytest.main()