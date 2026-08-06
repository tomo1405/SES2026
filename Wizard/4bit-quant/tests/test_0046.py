python
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt
import pytest

def task_func(df: pd.DataFrame):
    # Select only numeric columns
    df_numeric = df.select_dtypes(include=[np.number])
    # Replace missing values
    df_numeric = df_numeric.fillna(df_numeric.mean(axis=0))
    # Perform PCA
    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(df_numeric)
    principalDf = pd.DataFrame(
        data=principalComponents,
        columns=["Component 1", "Component 2"],
    )

    # Plot scatter plot
    ax = sns.scatterplot(data=principalDf, x="Component 1", y="Component 2")
    plt.show()
    return principalDf, ax

def test_task_func():
    # Test case 1: Test with valid input
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': ['a', 'b', 'c']})
    principalDf, ax = task_func(df)
    assert principalDf.shape == (3, 2)
    assert ax is not None

    # Test case 2: Test with missing values
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, None, 6], 'C': ['a', 'b', 'c', 'd']})
    principalDf, ax = task_func(df)
    assert principalDf.shape == (3, 2)
    assert ax is not None

    # Test case 3: Test with all missing values
    df = pd.DataFrame({'A': [None, None, None], 'B': [None, None, None], 'C': ['a', 'b', 'c']})
    principalDf, ax = task_func(df)
    assert principalDf.shape == (3, 2)
    assert ax is not None

    # Test case 4: Test with all same values
    df = pd.DataFrame({'A': [1, 1, 1], 'B': [4, 4, 4], 'C': ['a', 'b', 'c']})
    principalDf, ax = task_func(df)
    assert principalDf.shape == (3, 2)
    assert ax is not None

    # Test case 5: Test with invalid input
    with pytest.raises(TypeError):
        task_func('invalid input')