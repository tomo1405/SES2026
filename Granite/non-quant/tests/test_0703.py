import pandas as pd
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
import pytest

def task_func(df):
    pca = PCA(n_components=2)
    df_pca = pca.fit_transform(df)
    
    df_pca = pd.DataFrame(df_pca, columns=['PC1', 'PC2'])
    
    return df_pca

@pytest.mark.parametrize("df", [load_iris().data, pd.DataFrame(load_iris().data)])
def test_task_func(df):
    result = task_func(df)
    assert result.shape == (150, 2)
    assert result.columns.tolist() == ['PC1', 'PC2']