import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pytest

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
    # Test case 1: Input is not a DataFrame
    with pytest.raises(ValueError) as excinfo:
        task_func("not a DataFrame")
    assert "Input must be a DataFrame" in str(excinfo.value)

    # Test case 2: Input DataFrame is empty
    df = pd.DataFrame()
    with pytest.raises(ValueError) as excinfo:
        task_func(df)
    assert "DataFrame is empty" in str(excinfo.value)

    # Test case 3: Input DataFrame has valid data
    df = pd.DataFrame({
        'Feature 1': [1, 2, 3],
        'Feature 2': [4, 5, 6]
    })
    pca_df, ax = task_func(df)
    assert isinstance(pca_df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert pca_df.shape == (3, 2)
    assert ax.get_xlabel() == 'Principal Component 1'
    assert ax.get_ylabel() == 'Principal Component 2'
    assert ax.get_title() == '2 Component PCA'