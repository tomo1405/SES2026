import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt
from unittest.mock import patch

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
    # Create a sample DataFrame with numeric and non-numeric columns
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': ['a', 'b', 'c']
    })

    # Mock the show function to avoid showing the plot
    with patch('matplotlib.pyplot.show') as mock_show:
        # Call the task function
        principal_df, ax = task_func(df)

        # Assert that the returned DataFrame has the expected columns
        assert set(principal_df.columns) == {"Component 1", "Component 2"}

        # Assert that the scatter plot was called with the correct arguments
        ax.assert_called_with(data=principal_df, x="Component 1", y="Component 2")

        # Assert that the show function was called
        mock_show.assert_called()