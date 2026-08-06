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
        'A': [1, 2, np.nan, 4, 5],
        'B': [np.nan, 2, 3, 4, 5],
        'C': [1, 2, 3, 4, 5],
        'D': [1, 2, 3, 4, 5]
    })

    # Call the function and store the returned values
    principal_df, ax = task_func(df)

    # Perform assertions to test the function's behavior
    assert isinstance(principal_df, pd.DataFrame)
    assert ax.get_xlabel() == "Component 1"
    assert ax.get_ylabel() == "Component 2"
    assert ax.get_title() == "Principal Component Analysis"

if __name__ == "__main__":
    pytest.main()