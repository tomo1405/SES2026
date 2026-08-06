python
import pandas as pd
import seaborn as sns
from scipy.stats import zscore
import pytest

def task_func(data_matrix):
    z_scores = zscore(data_matrix, axis=1)
    feature_columns = ["Feature " + str(i + 1) for i in range(data_matrix.shape[1])]
    df = pd.DataFrame(z_scores, columns=feature_columns)
    df["Mean"] = df.mean(axis=1)
    correlation_matrix = df.corr()
    ax = sns.heatmap(correlation_matrix, annot=True, fmt=".2f")
    return df, ax

def test_task_func():
    # Test case 1: Test with a 2D matrix
    data_matrix = [[1, 2, 3], [4, 5, 6]]
    expected_df = pd.DataFrame([[0.0, -1.0, 1.0], [-1.0, 0.0, -1.0], [1.0, -1.0, 0.0]], columns=["Feature 1", "Feature 2", "Feature 3"])
    expected_df["Mean"] = expected_df.mean(axis=1)
    expected_correlation_matrix = expected_df.corr()
    expected_ax = sns.heatmap(expected_correlation_matrix, annot=True, fmt=".2f")
    df, ax = task_func(data_matrix)
    assert df.equals(expected_df)
    assert ax.equals(expected_ax)

    # Test case 2: Test with a 3D matrix
    data_matrix = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
    expected_df = pd.DataFrame([[0.0, -1.0, 1.0], [-1.0, 0.0, -1.0], [1.0, -1.0, 0.0]], columns=["Feature 1", "Feature 2", "Feature 3"])
    expected_df["Mean"] = expected_df.mean(axis=1)
    expected_correlation_matrix = expected_df.corr()
    expected_ax = sns.heatmap(expected_correlation_matrix, annot=True, fmt=".2f")
    df, ax = task_func(data_matrix)
    assert df.equals(expected_df)
    assert ax.equals(expected_ax)

    # Test case 3: Test with a 4D matrix
    data_matrix = [[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]], [[[13, 14, 15], [16, 17, 18]], [[19, 20, 21], [22, 23, 24]]]]
    expected_df = pd.DataFrame([[0.0, -1.0, 1.0], [-1.0, 0.0, -1.0], [1.0, -1.0, 0.0]], columns=["Feature 1", "Feature 2", "Feature 3"])
    expected_df["Mean"] = expected_df.mean(axis=1)
    expected_correlation_matrix = expected_df.corr()
    expected_ax = sns.heatmap(expected_correlation_matrix, annot=True, fmt=".2f")
    df, ax = task_func(data_matrix)
    assert df.equals(expected_df)
    assert ax.equals(expected_ax)