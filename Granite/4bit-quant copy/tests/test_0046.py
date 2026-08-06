import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt

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

import pytest

def test_task_func():
    # Create a sample DataFrame for testing
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]
    })

    # Call the function with the sample DataFrame
    principal_df, ax = task_func(df)

    # Assert the expected output
    assert isinstance(principal_df, pd.DataFrame)
    assert isinstance(ax, sns.axisgrid.AxisGrid)

if __name__ == "__main__":
    pytest.main()