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
    data_matrix = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    df, ax = task_func(data_matrix)
    assert df.shape == (3, 4)
    assert df.columns.tolist() == ["Feature 1", "Feature 2", "Feature 3", "Mean"]
    assert df["Mean"].tolist() == [0.0, 0.0, 0.0]
    assert ax.get_title() == "Correlation Matrix"
    assert ax.get_xlabel() == "Feature"
    assert ax.get_ylabel() == "Feature"