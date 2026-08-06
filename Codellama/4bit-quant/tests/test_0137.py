import matplotlib
import pandas as pd
import pytest
from src_0137 import task_func


def test_task_func():
    # Test 1: Input is not a DataFrame
    with pytest.raises(ValueError):
        task_func(1)

    # Test 2: Input DataFrame is empty
    with pytest.raises(ValueError):
        task_func(pd.DataFrame())

    # Test 3: Input DataFrame is not empty
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    pca_df, ax = task_func(df)
    assert isinstance(pca_df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert pca_df.shape == (3, 2)
    assert ax.get_xlabel() == 'Principal Component 1'
    assert ax.get_ylabel() == 'Principal Component 2'
    assert ax.get_title() == '2 Component PCA'