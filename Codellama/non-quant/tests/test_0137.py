import pytest
from src_0137 import task_func
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def test_task_func():
    # Test 1: Input is not a DataFrame
    with pytest.raises(ValueError):
        task_func(123)

    # Test 2: Input is an empty DataFrame
    with pytest.raises(ValueError):
        task_func(pd.DataFrame())

    # Test 3: Input is a valid DataFrame
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    pca_df, ax = task_func(df)
    assert isinstance(pca_df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert pca_df.shape == (3, 2)
    assert ax.get_xlabel() == 'Principal Component 1'
    assert ax.get_ylabel() == 'Principal Component 2'
    assert ax.get_title() == '2 Component PCA'