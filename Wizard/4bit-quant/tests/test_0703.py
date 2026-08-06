python
import pandas as pd
import pytest
from sklearn.decomposition import PCA
from src_0703 import task_func

def test_task_func():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    df_pca = task_func(df)
    assert df_pca.shape == (3, 2)
    assert df_pca.columns.tolist() == ['PC1', 'PC2']