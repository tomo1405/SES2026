python
import pytest
import matplotlib.pyplot as plt
import random
import string
import pandas as pd
import seaborn as sns

# Constants
LETTERS = list(string.ascii_lowercase)

def task_func(rows=1000, string_length=3):

    # Generate random strings
    data = ["".join(random.choices(LETTERS, k=string_length)) for _ in range(rows)]

    # Create a DataFrame and compute letter frequency
    df = pd.DataFrame({"String": data})

    # Check if the DataFrame is empty
    if df.empty:
        print("No data to generate heatmap.")
        return None

    df = pd.get_dummies(df["String"].apply(list).explode()).groupby(level=0).sum()

    # Calculate the correlation matrix
    corr = df.corr()

    # Create and return the heatmap
    ax = sns.heatmap(corr, annot=True, fmt=".2f")
    plt.close()  # Close the plot to prevent it from showing during function call
    return ax

def test_task_func():
    # Test case 1: Test with default values
    ax = task_func()
    assert isinstance(ax, type(None))

    # Test case 2: Test with custom values
    ax = task_func(rows=500, string_length=5)
    assert isinstance(ax, sns.matrix.ClusterGrid)
    assert ax.data.shape == (500, 5)
    assert ax.ax_heatmap.get_title() == "Correlation Matrix"
    assert ax.ax_heatmap.get_xlabel() == "String"
    assert ax.ax_heatmap.get_ylabel() == "String"
    assert ax.cbar.ax.get_ylabel() == "Correlation Coefficient"
    plt.close()  # Close the plot to prevent it from showing during function call