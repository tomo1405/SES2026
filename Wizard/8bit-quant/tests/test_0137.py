python
import pandas as pd
import pytest
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def task_func(df):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a DataFrame")
    if df.empty:
        raise ValueError("DataFrame is empty")

    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(df)

    pca_df = pd.DataFrame(data=principal_components, columns=['Principal Component 1', 'Principal Component 2'])

    fig, ax = plt.subplots()
    ax.scatter(pca_df['Principal Component 1'], pca_df['Principal Component 2'])
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2')
    ax.set_title('2 Component PCA')

    return pca_df, ax

def test_task_func():
    # Test case 1: Valid input
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
    with pytest.raises(ValueError):
        task_func(pd.DataFrame())