python
import pandas as pd
import pytest
from src_0137 import task_func

def test_task_func():
    # Test case 1: Valid input DataFrame
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    pca_df, ax = task_func(df)
    assert isinstance(pca_df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert pca_df.shape == (3, 2)
    assert ax.get_xlabel() == 'Principal Component 1'
    assert ax.get_ylabel() == 'Principal Component 2'
    assert ax.get_title() == '2 Component PCA'

    # Test case 2: Invalid input type
    with pytest.raises(ValueError):
        task_func(123)

    # Test case 3: Empty DataFrame
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df)